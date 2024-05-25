"""
factsheet for multi strategy report for cross sectional comparison of strategies
and generating sensitivities to parameters
see example in qis.examples.factheets.multi_strategy.py
in pybloqs\jinja\table.html in line 44 have this: {% for col_name, cell in row.items() %}
"""
# packages
import numpy as np
import pandas as pd
import pybloqs as p
import pybloqs.block.table_formatters as tf

# qis
import qis as qis
from qis import TimePeriod, PerfParams, BenchmarkReturnsQuantileRegimeSpecs
from qis.portfolio.multi_portfolio_data import MultiPortfolioData
from qis.portfolio.reports.config import PERF_PARAMS, REGIME_PARAMS
from qis.portfolio.reports.config import KWARGS_SUPTITLE, KWARGS_TITLE, KWARGS_TEXT, KWARGS_FOOTNOTE, KWARGS_FIG


def generate_strategy_benchmark_factsheet_with_pyblogs(multi_portfolio_data: MultiPortfolioData,
                                                       strategy_idx: int = 0,  # strategy is multi_portfolio_data[strategy_idx]
                                                       benchmark_idx: int = 1,  # benchmark is multi_portfolio_data[benchmark_idx]
                                                       time_period: TimePeriod = None,
                                                       time_period_last: TimePeriod = None,
                                                       perf_params: PerfParams = PERF_PARAMS,
                                                       regime_params: BenchmarkReturnsQuantileRegimeSpecs = REGIME_PARAMS,
                                                       benchmark: str = None,
                                                       backtest_name: str = None,
                                                       heatmap_freq: str = 'YE',
                                                       weight_freq: str = 'ME',
                                                       is_input_weights: bool = True,
                                                       fontsize: int = 4,
                                                       **kwargs
                                                       ) -> p.VStack:
    """
    this one is well suited for large backtests with over 100 strategies
    """
    if time_period is None:
        raise ValueError(f"pass non none time_period")
    if time_period_last is None:
        time_period_last = qis.get_time_period_shifted_by_years(time_period=time_period, n_years=1)

    if benchmark is None:
        benchmark = multi_portfolio_data.benchmark_prices.columns[0]

    # define axiliary vars
    strategy_name = multi_portfolio_data.portfolio_datas[strategy_idx].ticker
    benchmark_name = multi_portfolio_data.portfolio_datas[benchmark_idx].ticker
    asset_class_data = multi_portfolio_data.portfolio_datas[strategy_idx].group_data
    group_order = multi_portfolio_data.portfolio_datas[strategy_idx].group_order

    plot_kwargs = dict(fontsize=fontsize,
                       linewidth=0.5,
                       digits_to_show=1, sharpe_digits=2,
                       weight='normal',
                       markersize=1,
                       framealpha=0.75)
    kwargs = qis.update_kwargs(kwargs, plot_kwargs)

    # start building blocks
    blocks = [p.Paragraph(f"{backtest_name}", **KWARGS_SUPTITLE)]

    # get strategy weights
    strategy_pnl = multi_portfolio_data.portfolio_datas[strategy_idx].get_attribution_table_by_instrument(time_period=time_period,
                                                                                                          freq=weight_freq,
                                                                                                          is_input_weights=is_input_weights)
    benchmark_pnl = multi_portfolio_data.portfolio_datas[benchmark_idx].get_attribution_table_by_instrument(time_period=time_period,
                                                                                                            freq=weight_freq,
                                                                                                            is_input_weights=is_input_weights)

    strategy_weights = multi_portfolio_data.portfolio_datas[strategy_idx].get_weights(time_period=time_period,
                                                                                      freq=weight_freq,
                                                                                      is_input_weights=is_input_weights)
    benchmark_weights = multi_portfolio_data.portfolio_datas[benchmark_idx].get_weights(time_period=time_period,
                                                                                        freq=weight_freq,
                                                                                        is_input_weights=is_input_weights)

    # weights
    strategy_w = strategy_weights.iloc[-1, :].rename(strategy_name)
    benchmark_w = benchmark_weights.iloc[-1, :].rename(benchmark_name)
    delta_w = (strategy_w.subtract(benchmark_w)).rename(f"diff")

    strategy_dw = (strategy_weights.iloc[-1, :].subtract(strategy_weights.iloc[-2, :])).rename(f"delta {strategy_name}")
    benchmark_dw = (benchmark_weights.iloc[-1, :].subtract(benchmark_weights.iloc[-2, :])).rename(f"delta {benchmark_name}")
    
    weights = pd.concat([strategy_w, benchmark_w, delta_w, strategy_dw, benchmark_dw], axis=1)
    weights_by_ac = qis.agg_df_by_groups(df=weights.T, group_data=asset_class_data, group_order=group_order).T

    # attribution
    strategy_attrib_last = strategy_pnl.iloc[-1, :].rename(f"{strategy_name} last")
    benchmark_attrib_last = benchmark_pnl.iloc[-1, :].rename(f"{benchmark_name} last")
    strategy_attrib_3m = strategy_pnl.rolling(3).sum().iloc[-1, :].rename(f"{strategy_name} 3m")
    benchmark_attrib_3m = benchmark_pnl.rolling(3).sum().iloc[-1, :].rename(f"{benchmark_name} 3m")
    strategy_attrib_12m = strategy_pnl.rolling(12).sum().iloc[-1, :].rename(f"{strategy_name} 12m")
    benchmark_attrib_12m = benchmark_pnl.rolling(12).sum().iloc[-1, :].rename(f"{benchmark_name} 12m")
    attribs = pd.concat([strategy_attrib_last, benchmark_attrib_last,
                         strategy_attrib_3m, benchmark_attrib_3m,
                         strategy_attrib_12m, benchmark_attrib_12m], axis=1)

    attribs_by_ac = qis.agg_df_by_groups(df=attribs.T, group_data=asset_class_data, group_order=group_order).T
    attribs.loc['Total', :] = np.nansum(attribs, axis=0)
    attribs_by_ac.loc['Total', :] = np.nansum(attribs_by_ac, axis=0)

    # 1. weights table
    b_weights = p.Block([p.Paragraph(f"Instrument weights for {strategy_weights.index[-1]:'%d%b%Y'}", **KWARGS_TITLE),
                          p.Block(weights,
                                  formatters=[
                                      tf.FmtPercent(n_decimals=2, apply_to_header_and_index=False),
                                      tf.FmtReplaceNaN(value=''),
                                      tf.FmtHeatmap(columns=['diff']),  # , max_color=(255,0,255)
                                      tf.FmtAddCellBorder(each=1.0,
                                                          columns=weights.columns.to_list(),
                                                          color=tf.colors.GREY,
                                                          apply_to_header_and_index=True)
                                  ]),
                          p.Paragraph(f"  ", **KWARGS_FOOTNOTE)],
                         **KWARGS_TEXT)
    blocks.append(b_weights)

    # 2. weights by ac table
    b_weights2 = p.Block([p.Paragraph(f"Asset class weights for {strategy_weights.index[-1]:'%d%b%Y'}", **KWARGS_TITLE),
                          p.Block(weights_by_ac,
                                  formatters=[
                                      tf.FmtPercent(n_decimals=2, apply_to_header_and_index=False),
                                      tf.FmtReplaceNaN(value=''),
                                      tf.FmtHeatmap(columns=['diff']),  # , max_color=(255,0,255)
                                      tf.FmtAddCellBorder(each=1.0,
                                                          columns=weights_by_ac.columns.to_list(),
                                                          color=tf.colors.GREY,
                                                          apply_to_header_and_index=True)
                                  ]),
                          p.Paragraph(f"  ", **KWARGS_FOOTNOTE)],
                         **KWARGS_TEXT)
    blocks.append(b_weights2)

    # 3. attrib table
    b_attribs = p.Block([p.Paragraph(f"Attributions {strategy_weights.index[-1]:'%d%b%Y'}", **KWARGS_TITLE),
                          p.Block(attribs,
                                  formatters=[
                                      tf.FmtPercent(n_decimals=2, apply_to_header_and_index=False),
                                      tf.FmtReplaceNaN(value=''),
                                      tf.FmtHeatmap(columns=[f"{strategy_name} last", f"{benchmark_name} last"], rows=attribs.index[:-1]),
                                      tf.FmtHeatmap(columns=[f"{strategy_name} 3m", f"{benchmark_name} 3m"], rows=attribs.index[:-1]),
                                      tf.FmtHeatmap(columns=[f"{strategy_name} 12m", f"{benchmark_name} 12m"], rows=attribs.index[:-1]),
                                      tf.FmtAddCellBorder(each=1.0,
                                                          columns=attribs.columns.to_list(),
                                                          color=tf.colors.GREY,
                                                          apply_to_header_and_index=True)
                                  ]),
                          p.Paragraph(f"  ", **KWARGS_FOOTNOTE)],
                         **KWARGS_TEXT)
    blocks.append(b_attribs)

    # 4. attrib by ac table
    b_attribs2 = p.Block([p.Paragraph(f"Attributions by ac {strategy_weights.index[-1]:'%d%b%Y'}", **KWARGS_TITLE),
                          p.Block(attribs_by_ac,
                                  formatters=[
                                      tf.FmtPercent(n_decimals=2, apply_to_header_and_index=False),
                                      tf.FmtReplaceNaN(value=''),
                                      tf.FmtHeatmap(columns=[f"{strategy_name} last", f"{benchmark_name} last"], rows=attribs_by_ac.index[:-1]),
                                      tf.FmtHeatmap(columns=[f"{strategy_name} 3m", f"{benchmark_name} 3m"], rows=attribs_by_ac.index[:-1]),
                                      tf.FmtHeatmap(columns=[f"{strategy_name} 12m", f"{benchmark_name} 12m"], rows=attribs_by_ac.index[:-1]),
                                      tf.FmtAddCellBorder(each=1.0,
                                                          columns=attribs_by_ac.columns.to_list(),
                                                          color=tf.colors.GREY,
                                                          apply_to_header_and_index=True)
                                  ]),
                          p.Paragraph(f"  ", **KWARGS_FOOTNOTE)],
                         **KWARGS_TEXT)
    blocks.append(b_attribs2)

    """

    # 1. ra performance table
    column_header = 'Strategy'
    ra_perf_table = multi_portfolio_data.get_ra_perf_table(benchmark=benchmark,
                                                           drop_benchmark=True,
                                                           is_convert_to_str=False,
                                                           perf_params=perf_params,
                                                           time_period=time_period,
                                                           column_header=column_header,
                                                           **kwargs)
    ra_perf_table_last = multi_portfolio_data.get_ra_perf_table(benchmark=benchmark,
                                                                drop_benchmark=True,
                                                                is_convert_to_str=False,
                                                                perf_params=perf_params,
                                                                time_period=time_period_last,
                                                                column_header=column_header,
                                                                **kwargs)

    # highlight
    fmt_highlight_base = tf.FmtHighlightText(rows=[ra_perf_table.index[0]], bold=False, apply_to_header_and_index=False)
    fmt_highlight_index = tf.FmtHighlightText(columns=[column_header], bold=False, italic=False,
                                              font_color=tf.colors.DARK_BLUE, apply_to_header_and_index=True)

    tables = {time_period.to_str(): ra_perf_table, time_period_last.to_str(): ra_perf_table_last}

    b_ra_perf_tables = []
    for key, table in tables.items():
        b_ra_perf_table = p.Block([p.Paragraph(f"Risk-adjusted Performance table for {key}", **KWARGS_TITLE),
                                    p.Block(table,
                                            formatters=[
                                                tf.FmtPercent(n_decimals=2, columns=[PerfStat.TOTAL_RETURN.to_str(**kwargs),
                                                                                     PerfStat.PA_RETURN.to_str(**kwargs),
                                                                                     PerfStat.VOL.to_str(**kwargs),
                                                                                     PerfStat.MAX_DD.to_str(**kwargs),
                                                                                     PerfStat.ALPHA_AN.to_str(**kwargs),
                                                                                     PerfStat.R2.to_str(**kwargs)
                                                                                     ], apply_to_header_and_index=False),
                                                fmt_highlight_base,
                                                fmt_highlight_index,
                                                tf.FmtReplaceNaN(value=''),
                                                tf.FmtHeatmap(columns=[PerfStat.PA_RETURN.to_str(**kwargs),
                                                                       PerfStat.SHARPE_EXCESS.to_str(**kwargs),
                                                                       PerfStat.ALPHA_AN.to_str(**kwargs),
                                                                       PerfStat.BETA.to_str(**kwargs)]),
                                                tf.FmtHeatmap(columns=[PerfStat.MAX_DD.to_str(**kwargs),
                                                                       PerfStat.SKEWNESS.to_str(**kwargs)], max_color=(255,0,255)),
                                                tf.FmtAddCellBorder(each=1.0,
                                                                    columns=ra_perf_table.columns.to_list()[:1],
                                                                    color=tf.colors.GREY,
                                                                    apply_to_header_and_index=True)
                                            ]),
                                   p.Paragraph(f"  ", **KWARGS_FOOTNOTE)],
                                  **KWARGS_TEXT)
        b_ra_perf_tables.append(b_ra_perf_table)
    blocks.append([p.HStack(b_ra_perf_tables, cascade_cfg=False),
                   p.Paragraph(f" beta to {benchmark} ", **KWARGS_FOOTNOTE)])

    # 2. performance bars
    perf_columns = [PerfStat.SHARPE_EXCESS, PerfStat.MAX_DD, PerfStat.BETA]
    fig_size = qis.get_df_table_size(df=ra_perf_table)
    fig_perf_bar, axs = plt.subplots(1, len(perf_columns), figsize=(12, 1.2*fig_size[1]), constrained_layout=True)
    for idx, perf_column in enumerate(perf_columns):
        df = ra_perf_table[perf_column.to_str(**kwargs)].to_frame()
        colors = qis.compute_heatmap_colors(a=df.to_numpy())
        qis.plot_vbars(df=df,
                       var_format=perf_column.to_format(**kwargs),
                       title=perf_column.to_str(**kwargs),
                       legend_loc=None,
                       colors=colors,
                       is_category_names_colors=False,
                       ax=axs[idx],
                       **qis.update_kwargs(kwargs, dict(fontsize=8))
                       )
    b_fig_perf_bar = p.Block(
        [p.Paragraph(f"Performance statistics", **KWARGS_TITLE),
         p.Block(fig_perf_bar, **KWARGS_FIG)], **KWARGS_TEXT)
    blocks.append(b_fig_perf_bar)

    # 3. regime conditional
    fig_size = qis.get_df_table_size(df=ra_perf_table)
    fig_perf_regime, axs = plt.subplots(1, len(multi_portfolio_data.benchmark_prices.columns), figsize=(12, 1.2*fig_size[1]), constrained_layout=True)
    if len(multi_portfolio_data.benchmark_prices.columns) == 1:
        axs = [axs]
    for idx, benchmark in enumerate(multi_portfolio_data.benchmark_prices.columns):
        multi_portfolio_data.plot_regime_data(time_period=time_period,
                                              perf_params=perf_params,
                                              regime_params=regime_params,
                                              is_use_vbar=True,
                                              title=f"{benchmark}",
                                              benchmark=benchmark,
                                              ax=axs[idx],
                                              **qis.update_kwargs(kwargs, dict(fontsize=8)))
    b_fig_regime = p.Block(
        [p.Paragraph(f"Sharpe ratio split to {str(benchmark)} Bear/Normal/Bull {regime_params.freq}-freq regimes", **KWARGS_TITLE),
         p.Block(fig_perf_regime, **KWARGS_FIG)], **KWARGS_TEXT)
    blocks.append(b_fig_regime)

    # 4. heatmap of annual returns
    prices = multi_portfolio_data.get_navs(time_period=time_period)
    returns_ye = qis.compute_periodic_returns(prices=prices,
                                              freq=heatmap_freq,
                                              time_period=time_period,
                                              total_name='Total',
                                              add_total=True,
                                              **qis.update_kwargs(kwargs, dict(date_format='%Y'))
                                              ).T
    fmt_highlight_base = tf.FmtHighlightText(rows=[returns_ye.index[0]], bold=False, apply_to_header_and_index=False)
    fmt_highlight_index = tf.FmtHighlightText(columns=[returns_ye.index.name], bold=False, italic=False,
                                              font_color=tf.colors.DARK_BLUE, apply_to_header_and_index=True)

    b_returns_ye = p.Block([p.Paragraph(f"Annual returns table", **KWARGS_TITLE),
                            p.Block(returns_ye,
                                    formatters=[tf.FmtPercent(n_decimals=0, columns=returns_ye.columns, apply_to_header_and_index=False),
                                                fmt_highlight_base,
                                                fmt_highlight_index,
                                                tf.FmtReplaceNaN(value=''),
                                                tf.FmtHeatmap(columns=returns_ye.columns, axis=0)
                                                ]),
                            p.Paragraph(f"  ", **KWARGS_FOOTNOTE)],
                           **KWARGS_TEXT)
    blocks.append(b_returns_ye)

    # param sensetivity scatter
    if param_name is not None:
        ra_perf_table = multi_portfolio_data.get_ra_perf_table(benchmark=benchmark,
                                                               drop_benchmark=True,
                                                               is_convert_to_str=False,
                                                               perf_params=perf_params,
                                                               time_period=time_period,
                                                               column_header=column_header,
                                                               **kwargs)

        if 'base' in ra_perf_table.index:
            ra_perf_table = ra_perf_table.drop('base', axis=0)

        hue_name = 'group'

        xy = ra_perf_table.copy()
        xy[hue_name] = [x.split(' ')[0] for x in ra_perf_table.index]
        xy[param_name] = [float(x.split('=')[-1]) for x in ra_perf_table.index]
        x_limits = (np.nanmin(xy[param_name]), np.nanmax(xy[param_name]))

        fig_scatter1, ax = plt.subplots(1, 1, figsize=(14, 4.5), constrained_layout=True)
        qis.plot_scatter(df=xy, x=param_name, y=PerfStat.SHARPE_EXCESS.to_str(**kwargs), hue=hue_name,
                         title=f"Sharpe",
                         var_format='{:.2f}',
                         x_limits=x_limits,
                         ax=ax,
                         **kwargs)
        b_fig_scatter1 = p.Block([p.Paragraph(f"Scatter of {PerfStat.SHARPE_EXCESS.to_str()} for {param_name} sensitivity", **KWARGS_TITLE),
                                p.Block(fig_scatter1, **KWARGS_FIG)],
                               **KWARGS_TEXT)
        blocks.append(b_fig_scatter1)

        fig_scatter2, ax = plt.subplots(1, 1, figsize=(14, 4.5), constrained_layout=True)
        qis.plot_scatter(df=xy, x=param_name, y=PerfStat.MAX_DD.to_str(**kwargs), hue=hue_name,
                         title=f"Max DD",
                         var_format='{:.2%}',
                         x_limits=x_limits,
                         ax=ax,
                         **kwargs)
        b_fig_scatter = p.Block([p.Paragraph(f"Scatter of {PerfStat.MAX_DD.to_str(**kwargs)} for {param_name} sensitivity", **KWARGS_TITLE),
                                 p.Block(fig_scatter2, **KWARGS_FIG)],
                                **KWARGS_TEXT)
        blocks.append(b_fig_scatter)
    """

    report = p.VStack(blocks, cascade_cfg=False)
    return report

"""
def generate_multi_portfolio_factsheet(multi_portfolio_data: MultiPortfolioData,
                                       time_period: TimePeriod = None,
                                       perf_params: PerfParams = PERF_PARAMS,
                                       regime_params: BenchmarkReturnsQuantileRegimeSpecs = REGIME_PARAMS,
                                       regime_benchmark: str = None,
                                       backtest_name: str = None,
                                       heatmap_freq: str = 'YE',
                                       figsize: Tuple[float, float] = (8.3, 11.7),  # A4 for portrait
                                       is_grouped: bool = False,
                                       fontsize: int = 4,
                                       **kwargs
                                       ) -> plt.Figure:
    # for portfolio data with structurally different strategies
    # for portfolios with large universe use is_grouped = True to report tunrover and exposures by groups
    
    if regime_benchmark is None:
        regime_benchmark = multi_portfolio_data.benchmark_prices.columns[0]

    plot_kwargs = dict(fontsize=fontsize,
                       linewidth=0.5,
                       digits_to_show=1, sharpe_digits=2,
                       weight='normal',
                       markersize=1,
                       framealpha=0.75)
    kwargs = qis.update_kwargs(kwargs, plot_kwargs)

    fig = plt.figure(figsize=figsize, constrained_layout=True)
    gs = fig.add_gridspec(nrows=7, ncols=4, wspace=0.0, hspace=0.0)

    if backtest_name is not None:
        fig.suptitle(backtest_name, fontweight="bold", fontsize=8, color='blue')

    multi_portfolio_data.plot_nav(ax=fig.add_subplot(gs[0, :2]),
                                  time_period=time_period,
                                  regime_benchmark=regime_benchmark,
                                  perf_params=perf_params,
                                  regime_params=regime_params,
                                  title='Cumulative performance',
                                  **kwargs)

    multi_portfolio_data.plot_drawdowns(ax=fig.add_subplot(gs[1, :2]),
                                        time_period=time_period,
                                        regime_benchmark=regime_benchmark,
                                        regime_params=regime_params,
                                        title='Running Drawdowns',
                                        **kwargs)

    multi_portfolio_data.plot_rolling_time_under_water(ax=fig.add_subplot(gs[2, :2]),
                                                       time_period=time_period,
                                                       regime_benchmark=regime_benchmark,
                                                       regime_params=regime_params,
                                                       title='Rolling time under water',
                                                       **kwargs)

    multi_portfolio_data.plot_exposures(ax=fig.add_subplot(gs[3, :2]),
                                        portfolio_idx=0,
                                        time_period=time_period,
                                        benchmark=regime_benchmark,
                                        regime_params=regime_params,
                                        **kwargs)

    multi_portfolio_data.plot_turnover(ax=fig.add_subplot(gs[4, :2]),
                                       time_period=time_period,
                                       benchmark=regime_benchmark,
                                       regime_params=regime_params,
                                       **kwargs)

    multi_portfolio_data.plot_costs(ax=fig.add_subplot(gs[5, :2]),
                                    time_period=time_period,
                                    benchmark=regime_benchmark,
                                    regime_params=regime_params,
                                    **kwargs)

    # select two benchmarks for factor exposures
    multi_portfolio_data.plot_factor_betas(axs=[fig.add_subplot(gs[6, :2]), fig.add_subplot(gs[6, 2:])],
                                           benchmark_prices=multi_portfolio_data.benchmark_prices.iloc[:, :2],
                                           time_period=time_period,
                                           regime_benchmark=regime_benchmark,
                                           regime_params=regime_params,
                                           **kwargs)

    multi_portfolio_data.plot_performance_bars(ax=fig.add_subplot(gs[0, 2]),
                                               perf_params=perf_params,
                                               perf_column=PerfStat.SHARPE_EXCESS,
                                               time_period=time_period,
                                               **qis.update_kwargs(kwargs, dict(fontsize=fontsize)))

    multi_portfolio_data.plot_performance_bars(ax=fig.add_subplot(gs[0, 3]),
                                               perf_params=perf_params,
                                               perf_column=PerfStat.MAX_DD,
                                               time_period=time_period,
                                               **qis.update_kwargs(kwargs, dict(fontsize=fontsize)))

    multi_portfolio_data.plot_ra_perf_table(ax=fig.add_subplot(gs[1, 2:]),
                                            perf_params=perf_params,
                                            time_period=time_period,
                                            **qis.update_kwargs(kwargs, dict(fontsize=fontsize)))

    multi_portfolio_data.plot_periodic_returns(ax=fig.add_subplot(gs[2, 2:]),
                                               heatmap_freq=heatmap_freq,
                                               title=f"{heatmap_freq} returns",
                                               time_period=time_period,
                                               **qis.update_kwargs(kwargs, dict(fontsize=fontsize)))

    multi_portfolio_data.plot_corr_table(ax=fig.add_subplot(gs[3, 2:]),
                                         time_period=time_period,
                                         freq='W-WED',
                                         **qis.update_kwargs(kwargs, dict(fontsize=fontsize)))

    multi_portfolio_data.plot_regime_data(ax=fig.add_subplot(gs[4, 2:]),
                                          is_grouped=False,
                                          time_period=time_period,
                                          perf_params=perf_params,
                                          regime_params=regime_params,
                                          benchmark=multi_portfolio_data.benchmark_prices.columns[0],
                                          **kwargs)
    multi_portfolio_data.plot_regime_data(ax=fig.add_subplot(gs[5, 2:]),
                                          is_grouped=False,
                                          time_period=time_period,
                                          perf_params=perf_params,
                                          regime_params=regime_params,
                                          benchmark=multi_portfolio_data.benchmark_prices.columns[1],
                                          **kwargs)
    return fig
"""
