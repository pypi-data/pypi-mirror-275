from collections import UserDict
import re
from typing import Iterable, Optional
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class ColorWheelDict(UserDict):
    """Lookup dictionary that maps keys to hex colors by using a color wheel.

    When a key is not present the first color of the color wheel is added as the value,
    and the color is moved from the beginning to the end of the color wheel. If no list
    of colors is specified, a default list of ten colors is added to the color wheel.
    It is also possible to manually set key and color pairs by using the same syntax as
    for a regular dictionary.
    """

    def __init__(self, colors: Optional[list[str]] = None):
        """Initializes a ColorWheelDict.

        Args:
            colors: Optional, a list of hex colors used for the color wheel. By default
                a list with ten colors is used.
        """
        self.data = {}

        if colors is not None:
            self.colors = colors
        else:
            self.colors = [
                "#80b1d3",
                "#fdb462",
                "#8dd3c7",
                "#bebada",
                "#fb8072",
                "#b3de69",
                "#fccde5",
                "#d9d9d9",
                "#bc80bd",
                "#ccebc5",
            ]
        self._color_wheel = self.colors.copy()

    def _next_color(self) -> str:
        color = self._color_wheel.pop(0)
        self._color_wheel.append(color)
        return color

    def __setitem__(self, key, value):
        is_hexcolor = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", value)
        if is_hexcolor:
            self.data[key] = value
        else:
            raise ValueError(f"the specified value {value} is not a hexcolor.")

    def __getitem__(self, key):
        if key not in self.data:
            self.data[key] = self._next_color()
        return self.data[key]


def facet_channel_distribution(
    data: pd.DataFrame,
    channel: str,
    split_on: str,
    group_by: str = None,
    hue: str = None,
    density: bool = True,
    kind: str = "hist",
) -> list[(plt.Figure, list[plt.Axes])]:
    """Plots signal distributions of a FACS channel, one figure per split group.

    Args:
        data: Dataset for plotting.
        channel: Column in 'data' that will be plotted.
        split_on: Column used to group data into different figures.
        group_by: Optional, specifies a column that is used to group data into
            different subplots.
        hue: Optional, specifies a column that is used to group data within each
            subplot, generating one distribution per unique variable.
        density: Default True. If true, the bins of each distribution are normalized to
            the total number of counts and the bin width, so that the area under the
            histogram integrates to 1
        kind: "hist" or "kde", default "hist. Whether to plot a histogram or a gaussian
            kernel density estimate. Note that "kde" is considerably slower and might
            not always work.

    Returns:
        List of tuples, each containing a Matplotlib figure object and a list of
        matplotlib axes objects. Figures correspond to groups defined by 'split_on',
        and axes to groups defined by 'group_by'.
    """

    figures = []
    for group_name, group_data in data.groupby(split_on):
        fig, axes = channel_distribution(
            group_data,
            channel,
            group_by=group_by,
            hue=hue,
            kind=kind,
            density=density,
        )
        fig.suptitle(f"{split_on}: {group_name}", fontsize=12)
        fig.subplots_adjust(top=0.85)
        figures.append((fig, axes))
    xlims = [[], []]
    for fig, axes in figures:
        xlims[0].append(axes[0].get_xlim()[0])
        xlims[1].append(axes[0].get_xlim()[1])
    xlims = (min(xlims[0]), max(xlims[1]))
    [axes[0].set_xlim(xlims) for fig, axes in figures]
    return figures


def channel_distribution(
    data: pd.DataFrame,
    channel: str,
    group_by: str = None,
    hue: str = None,
    kind: str = "hist",
    density: bool = True,
) -> (plt.Figure, list[plt.Axes]):
    """Plot signal distributions of a FACS channel.

    Args:
        data: Dataset for plotting.
        channel: Column in 'data' that will be plotted.
        group_by: Optional, specifies a column that is used to group data into different
            subplots.
        hue: Optional, specifies a column that is used to group data within each
            subplot, generating one distribution per unique variable.
        density: Default True. If true, the bins of each distribution are normalized to
            the total number of counts and the bin width, so that the area under the
            histogram integrates to 1
        kind: "hist" or "kde", default "hist. Whether to plot a histogram or a gaussian
            kernel density estimate. Note that "kde" is considerably slower and might
            not always work.

    Returns:
        A matplotlib figure object and a list of matplotlib axes objects. Axes
        correspond to groups defined by 'sub_group'.
    """
    color_mapping = ColorWheelDict()
    if hue is not None:
        colors = {r: color_mapping[r] for r in data[hue].unique()}
    else:
        colors = color_mapping.colors[0]

    if group_by is not None:
        num_plots = len(data[group_by].unique())
        data_sets = data.groupby(group_by)
    else:
        num_plots = 1
        data_sets = [("", data)]
    ylabel = "Cell density" if density else "Cell number"

    bins = np.linspace(data[channel].min() * 0.98, data[channel].max() * 1.02, 50)

    plotheight = 2.5
    legendheight = 1.2
    figheight = plotheight + legendheight
    figwidth = num_plots * 3
    figsize = (figwidth, figheight)

    sns.set_style("whitegrid")
    fig, axes = plt.subplots(1, num_plots, figsize=figsize, sharex=True, sharey=True)
    axes = axes if isinstance(axes, Iterable) else (axes,)

    for pos, (group_name, group_data) in enumerate(data_sets):
        ax = axes[pos]
        if kind == "kde":
            sns.kdeplot(
                data=group_data,
                x=channel,
                hue=hue,
                legend=True,
                common_norm=True,
                palette=colors,
                fill=True,
                ax=ax,
            )
        elif kind == "hist":
            if hue is not None:
                plot_data = []
                label = []
                for replicate, rep_data in group_data.groupby(hue):
                    plot_data.append(rep_data[channel])
                    label.append(replicate)
                plot_color = [colors[replicate] for replicate in label]
            else:
                plot_data = group_data[channel]
                plot_color = colors
                label = None
            ax.hist(
                plot_data, density=density, histtype="step", bins=bins, color=plot_color
            )
            ax.hist(
                plot_data,
                density=density,
                histtype="stepfilled",
                bins=bins,
                label=label,
                color=plot_color,
                alpha=0.3,
                lw=0,
            )
            ax.set_xlabel(channel)
            if hue is not None:
                ax.legend(title=hue)
        else:
            sns.histplot(
                data=group_data,
                x=channel,
                hue=hue,
                bins=bins,
                legend=True,
                common_norm=True,
                element="step",
                palette=colors,
                ax=ax,
            )

        ax.grid(axis="x")
        ax.tick_params(axis="x", which="minor", bottom=True)
        ax.tick_params(axis="y", which="minor", bottom=True)
        ax.set_title(group_name)

    # Formats axis labels and gridlines
    axes[0].set_yticks([])
    axes[0].set_ylabel(ylabel)
    for ax_pos, ax in enumerate(axes):
        for spine in ["bottom", "left"]:
            ax.spines[spine].set_color("#000000")
            ax.spines[spine].set_linewidth(1)
        ax.grid(False, axis="y")
        ax.grid(axis="x", linestyle="dashed", linewidth=1, color="#cccccc")
    sns.despine(top=True, right=True)

    # Movse legend to the bottom of the plot
    fig.tight_layout()
    if hue is not None:
        for ax in axes:
            old_legend = ax.legend_
            legend_handles = old_legend.legendHandles
            legend_labels = [t.get_text() for t in old_legend.get_texts()]
            legend_title = old_legend.get_title().get_text()
            old_legend.remove()
        if len(axes) == 1:
            ncol = 2
        else:
            ncol = max([3, min([5, len(legend_labels)])])
        fig.legend(
            legend_handles,
            legend_labels,
            title=legend_title,
            bbox_to_anchor=(0.5, 0),
            ncol=ncol,
            loc="lower center",
        )
        figure_space_for_legend = legendheight / figheight
        fig.subplots_adjust(bottom=figure_space_for_legend)
    return fig, axes


def replicate_boxplots(
    data: pd.DataFrame,
    channel: str,
    group_by: str = "Condition",
    split_on: Optional[str] = None,
    order: Optional[list[str]] = None,
    showmeans: bool = False,
) -> (plt.Figure, list[plt.Axes]):
    """Box plots for each replicate and sub group, one figure per main group.

    Args:
        data: Dataset for plotting.
        channel: Column in 'data' for plotting
        group_by: Default "Condition". Specifies a column that is used together with
            the "Replicate" to group data. Each group is shown as a separate box plot.
        split_on: Optional, column used to split data into different subplots.
        order: Optional, allows specifying a list of sub groups and their order for
            plotting. Values must be present in the column specified by sub group.
        showmeans: Optional, if true means are displayed on top of boxplots.

    Returns:
        A matplotlib figure object and a list of matplotlib axes objects. Axes
        correspond to groups defined by 'split_on'.
    """
    if order is None:
        group_order = sorted(data[group_by].unique())
    else:
        group_order = order
    if split_on is None:
        num_plots = 1
        data_groups = [(None, data)]
    else:
        num_plots = len(data[split_on].unique())
        data_groups = data.groupby(split_on)

    replicate_order = sorted(data["Replicate"].unique())

    plotheight = 2.8
    legendheight = 0.6
    figheight = plotheight + legendheight
    figwidth = num_plots * len(group_order) + (0.15 * num_plots)
    figsize = (figwidth, figheight)

    meanprops = {
        "marker": "o",
        "markersize": "7",
        "markerfacecolor": "white",
        "markeredgecolor": "black",
    }
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, num_plots, figsize=figsize, sharex=True, sharey=True)
    axes = axes if isinstance(axes, Iterable) else (axes,)
    for pos, (group_name, group_data) in enumerate(data_groups):
        ax = axes[pos]
        sns.boxplot(
            data=group_data,
            x=group_by,
            y=channel,
            hue="Replicate",
            order=group_order,
            hue_order=replicate_order,
            ax=ax,
            showfliers=False,
            color="#808080",
            linewidth=1.25,
            showmeans=showmeans,
            meanprops=meanprops,
        )
        if pos != 0:
            ax.set_ylabel("")
        ax.legend(loc="upper left")
        ax.set_title(group_name)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

        for spine in ["bottom", "left"]:
            ax.spines[spine].set_color("#000000")
            ax.spines[spine].set_linewidth(1)
        ax.grid(False, axis="x")
        ax.grid(axis="y", linestyle="dashed", linewidth=1, color="#cccccc")
        sns.despine(top=True, right=True)
    fig.tight_layout()
    fig.subplots_adjust(wspace=0.15)
    return fig, axes


def replicate_summary(
    data: pd.DataFrame,
    on: str,
    group_by: str = "Condition",
    split_on: Optional[str] = None,
    order: Optional[list[str]] = None,
) -> (plt.Figure, list[plt.Axes]):
    """Plots experiment summary by showing mean values and individual replicate points.

    Generates one subplot per cell line. Plots for each condition the replicate mean
    as a box plot, and individual replicate data points as scatter points.

    Args:
        data: Dataset for plotting.
        on: Variable in 'data' for plotting.
        split_on: Optional, column used to split data into different subplots.
        group_by: Default "Condition". Specifies a column that is used to group data.
            Each group mean is shown as a separate bar plot, and individual data points
            are shown as scatter points.
        order: Optional, allows specifying a list of sub groups and their order for
            plotting. Values must be present in the column specified by sub group.

    Returns:
        Matplotlib figure object and a list of matplotlib axes objects.
    """
    if order is None:
        group_order = sorted(data[group_by].unique())
    else:
        group_order = order
    if split_on is None:
        num_plots = 1
        data_groups = [(None, data)]
    else:
        num_plots = len(data[split_on].unique())
        data_groups = data.groupby(split_on)

    plotheight = 2.5
    legendheight = 0.8
    figheight = plotheight + legendheight
    plotwidth = 0.5 * num_plots * len(group_order)
    spacingwidth = 0.75 * (num_plots - 1)
    figwidth = plotwidth + spacingwidth + 0.25
    figsize = (figwidth, figheight)

    color_mapping = ColorWheelDict()
    colors = {c: color_mapping[c] for c in group_order}
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, num_plots, figsize=figsize, sharex=True, sharey=True)
    axes = axes if isinstance(axes, Iterable) else (axes,)
    for pos, (group_name, group_data) in enumerate(data_groups):
        ax = axes[pos]
        sns.barplot(
            data=group_data,
            x=group_by,
            y=on,
            order=group_order,
            alpha=1,
            ci=None,
            edgecolor="#000000",
            linewidth=0.75,
            ax=ax,
            palette=colors,
        )
        sns.swarmplot(
            data=group_data,
            x=group_by,
            y=on,
            order=group_order,
            dodge=False,
            edgecolor="#000000",
            linewidth=0.75,
            ax=ax,
            palette=colors,
        )
        if pos != 0:
            ax.set_ylabel("")
        ax.set_title(group_name)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

        for spine in ["bottom", "left"]:
            ax.spines[spine].set_color("#000000")
            ax.spines[spine].set_linewidth(1)
        ax.grid(False, axis="x")
        ax.grid(axis="y", linestyle="dashed", linewidth=1, color="#cccccc")
        sns.despine(top=True, right=True)
    fig.tight_layout()
    fig.subplots_adjust(wspace=0.75)
    return fig, axes


def set_dpi(dpi: int) -> None:
    """Changes the default dots per inch settings for matplotlib plots.

    This effectively makes figures smaller or larger, without affecting the relative
    sizes of elements within the figures.

    Args:
        dpi: New default dots per inch.
    """
    plt.rcParams["figure.dpi"] = dpi
