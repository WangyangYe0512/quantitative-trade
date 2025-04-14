# Freqtrade 中文翻译修改记录

本文档记录了对 Freqtrade 进行的中文翻译修改,以便在版本更新后能够快速恢复翻译。

## Telegram 消息翻译

### freqtrade/rpc/telegram.py

这个文件包含了大量的 Telegram 消息翻译,以下是主要的翻译部分：

```python
# 帮助文本
help_message = (
    "*/start:* 启动交易者\n"
    "*/stop:* 停止交易者\n"
    "*/reload_config:* 重新加载配置文件\n"
    "*/status <交易ID>|[表格]:* 打印交易者状态和活跃交易状态,\n"
    "    可选择指定交易ID或添加'表格'参数\n"
    "*/status table:* 以表格形式打印活跃交易状态\n"
    "*/trades [表格]:* 打印所有交易的统计信息,\n"
    "    可选择添加'表格'参数\n"
    "*/profit:* 打印利润摘要\n"
    "*/forcesell <交易ID>|all:* 立即卖出交易（以当前价格)\n"
    "*/forcebuy <币对> [价格]:* 立即买入指定币对\n"
    "*/trades:* 打印所有完成的交易的统计信息\n"
    "*/delete <交易ID>:* 删除指定的交易\n"
    "*/count:* 显示活跃交易数量与允许的最大交易数量\n"
    "*/locks:* 显示当前被锁定的币对\n"
    "*/unlock <币对|ID>:* 解锁指定的币对（或锁定ID)\n"
    "*/balance:* 显示钱包余额\n"
    "*/daily <n>:* 显示过去n天的利润（默认为7)\n"
    "*/weekly:* 显示每周的累计利润\n"
    "*/monthly:* 显示每月的累计利润\n"
    "*/whitelist:* 显示当前的白名单\n"
    "*/blacklist [币对]:* 显示当前的黑名单,\n"
    "    可选择添加币对到黑名单\n"
    "*/blacklist_delete <币对>:* 从黑名单中删除指定币对\n"
    "*/logs [行数]:* 显示最后n行日志（默认为10)\n"
    "*/edge:* 显示边缘统计信息\n"
    "*/help:* 显示此消息\n"
    "*/version:* 显示版本\n"
)

# 状态消息
status_table_header = [
    "交易ID",
    "币对",
    "盈亏比",
    "当前价格",
    "目标",
    "止损",
    "已开仓",
]

# 交易消息
trades_table_header = [
    "交易ID",
    "币对",
    "盈亏比",
    "收益",
    "开仓时间",
    "关仓时间",
]

# 余额消息
balance_dust_level = 0.01
balance_table_header = [
    "币种",
    "可用余额",
    "总余额",
    "已用余额",
    "估值",
    "交易中",
]

# 黑名单消息
blacklist_table_header = [
    "币对",
    "直到",
    "原因",
]

# 白名单消息
whitelist_table_header = [
    "币对",
]

# 各种状态消息
status_msg = "*状态:* `{status}`"

# 警告消息
warning_msg = "⚠️ *警告:* `{status}`"

# 成功消息
success_msg = "✅ *成功:* `{status}`"

# 各种交易状态消息
trade_status_msg = (
    "*{exchange}:* `{pair}`\n"
    "*类型:* `{type}`\n"
    "*方向:* `{direction}`\n"
    "*状态:* `{status}`\n"
    "*金额:* `{amount}`\n"
    "*开仓价:* `{open_rate}`\n"
    "*当前价:* `{current_rate}`\n"
    "*盈亏比:* `{profit_ratio:.2%}`"
)

# 取消订单消息
order_cancel_msg = (
    "*交易* `#{trade_id}` *取消订单* `{order_id}`\n"
    "*原因:* `{reason}`"
)

# 各种交易消息
trade_open_msg = (
    "*{exchange}:* `{pair}`\n"
    "*类型:* `{type}`\n"
    "*方向:* `{direction}`\n"
    "*金额:* `{amount}`\n"
    "*开仓价:* `{open_rate}`\n"
    "*杠杆:* `{leverage}x`\n"
    "*标签:* `{enter_tag}`"
)

trade_close_msg = (
    "*{exchange}:* `{pair}`\n"
    "*类型:* `{type}`\n"
    "*方向:* `{direction}`\n"
    "*盈亏比:* `{profit_ratio:.2%}`\n"
    "*盈亏:* `{profit_amount} {stake_currency} ({profit_fiat})`\n"
    "*开仓价:* `{open_rate}`\n"
    "*关仓价:* `{close_rate}`\n"
    "*杠杆:* `{leverage}x`\n"
    "*标签:* `{enter_tag}`\n"
    "*关仓原因:* `{exit_reason}`"
)

# 各种错误消息
error_msg = "❌ *错误:* `{error}`"

# 各种警告消息
warning_msg = "⚠️ *警告:* `{warning}`"
```

## 状态文本翻译

### 1. freqtrade/rpc/rpc.py

```python
# _rpc_start 方法
def _rpc_start(self) -> dict[str, str]:
    """Handler for start"""
    if self._freqtrade.state == State.RUNNING:
        return {"status": "已经在运行中"}

    self._freqtrade.state = State.RUNNING
    return {"status": "正在启动交易者..."}

# _rpc_stop 方法
def _rpc_stop(self) -> dict[str, str]:
    """Handler for stop"""
    if self._freqtrade.state != State.STOPPED:
        self._freqtrade.state = State.STOPPED
        return {"status": "正在停止交易者..."}

    return {"status": "已经停止"}

# _rpc_reload_config 方法
def _rpc_reload_config(self) -> dict[str, str]:
    """Handler for reload_config."""
    self._freqtrade.state = State.RELOAD_CONFIG
    return {"status": "正在重新加载配置..."}

# _rpc_pause 方法
def _rpc_pause(self) -> dict[str, str]:
    """
    Handler to pause trading (stop entering new trades), but handle open trades gracefully.
    """
    if self._freqtrade.state == State.RUNNING:
        self._freqtrade.state = State.PAUSED

    if self._freqtrade.state == State.STOPPED:
        self._freqtrade.state = State.PAUSED
        return {
            "status": (
                "以暂停状态启动机器人,不会进行新入场。"
                "运行 /start 来启用入场。"
            )
        }

    return {
        "status": "已暂停,从现在起不会进行新入场。运行 /start 来启用入场。"
    }
```

### 2. freqtrade/worker.py

```python
# 状态通知
self._notify("WATCHDOG=1\nSTATUS=状态: 已停止.")

# 运行状态
state_str = "运行中" if state == State.RUNNING else "暂停"
self._notify(f"WATCHDOG=1\nSTATUS=状态: {state_str}.")

# 心跳消息
logger.info(f"机器人心跳. PID={getpid()}, 版本='{version}', 状态='{state.name}'")

# 错误提示
hint = "如果您认为重启是安全的,请发送 `/start`。"

# 进程终止消息
self.freqtrade.notify_status("进程已终止")
```

### 3. freqtrade/enums/state.py

```python
def __str__(self):
    state_names = {
        'RUNNING': '运行中',
        'PAUSED': '暂停',
        'STOPPED': '已停止',
        'RELOAD_CONFIG': '重新加载配置'
    }
    return state_names.get(self.name, f"{self.name.lower()}")
```

## 配对列表描述翻译

### 1. freqtrade/plugins/pairlist/MarketCapPairList.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    num = self._number_assets
    rank = self._max_rank
    msg = f"{self.name} - 从市值排名前 {rank} 中选取 {num} 个交易对"
    return msg
```

### 2. freqtrade/plugins/pairlist/RemotePairList.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    return f"{self.name} - 从远程配对列表中获取 {self._pairlistconfig['number_assets']} 个交易对"
```

### 3. freqtrade/plugins/pairlist/FullTradesFilter.py

```python
def short_desc(self) -> str:
    """
    Short allowlist method description - used for startup-messages
    """
    return f"{self.name} - 当交易槽位已满时缩减白名单。"
```

### 4. freqtrade/plugins/pairlist/OffsetFilter.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    if self._number_pairs:
        return f"{self.name} - 从偏移量 {self._offset} 开始选取 {self._number_pairs} 个交易对"
    return f"{self.name} - 将交易对列表偏移 {self._offset} 个位置"
```

### 5. freqtrade/plugins/pairlist/ShuffleFilter.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    return f"{self.name} - 每 {self._shuffle_freq} 随机打乱交易对" + (
        f", 种子值 = {self._seed}。" if self._seed is not None else "。"
    )
```

### 6. freqtrade/plugins/pairlist/PerformanceFilter.py

```python
def short_desc(self) -> str:
    """
    Short allowlist method description - used for startup-messages
    """
    return f"{self.name} - 按照性能对交易对进行排序。"
```

### 7. freqtrade/plugins/pairlist/PercentChangePairList.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    return f"{self.name} - 按百分比变化排名前 {self._pairlistconfig['number_assets']} 的交易对。"
```

### 8. freqtrade/plugins/pairlist/AgeFilter.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    return (
        f"{self.name} - 过滤上市天数少于 "
        f"{self._min_days_listed} {plural(self._min_days_listed, '天')}"
    ) + (
        f" 或者多于 {self._max_days_listed} {plural(self._max_days_listed, '天')}"
        if self._max_days_listed
        else ""
    )
```

### 9. freqtrade/plugins/pairlist/SpreadFilter.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    return (
        f"{self.name} - 过滤卖价/买价差超过 {self._max_spread_ratio:.2%} 的交易对。"
    )
```

### 10. freqtrade/plugins/pairlist/rangestabilityfilter.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    max_rate_desc = ""
    if self._max_rate_of_change:
        max_rate_desc = f" 和高于 {self._max_rate_of_change}"
    return (
        f"{self.name} - 过滤变化率低于 "
        f"{self._min_rate_of_change}{max_rate_desc} 的交易对,"
        f"基于过去 {plural(self._days, '天')}的数据。"
    )
```

### 11. freqtrade/plugins/pairlist/PrecisionFilter.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    return f"{self.name} - 过滤无法交易的币对。"
```

### 12. freqtrade/plugins/pairlist/VolatilityFilter.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    return (
        f"{self.name} - 过滤波动率在范围 "
        f"{self._min_volatility}-{self._max_volatility} "
        f"内的交易对,基于过去 {self._days} {plural(self._days, '天')}的数据。"
    )
```

### 13. freqtrade/plugins/pairlist/VolumePairList.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    return f"{self.name} - 按交易量排名前 {self._pairlistconfig['number_assets']} 的交易对。"
```

### 14. freqtrade/plugins/pairlist/PriceFilter.py

```python
def short_desc(self) -> str:
    """
    Short whitelist method description - used for startup-messages
    """
    active_price_filters = []
    if self._low_price_ratio != 0:
        active_price_filters.append(f"低于 {self._low_price_ratio:.1%}")
    if self._min_price != 0:
        active_price_filters.append(f"低于 {self._min_price:.8f}")
    if self._max_price != 0:
        active_price_filters.append(f"高于 {self._max_price:.8f}")
    if self._max_value != 0:
        active_price_filters.append(f"价值高于 {self._max_value:.8f}")

    if len(active_price_filters):
        return f"{self.name} - 过滤价格{' 或 '.join(active_price_filters)}的交易对。"

    return f"{self.name} - 未配置价格过滤器。"
```

## 其他翻译

### freqtrade/constants.py

```python
# 取消订单原因
CANCEL_REASON = {
    "TIMEOUT": "超时",
    "STOPLOSS_ON_EXCHANGE": "交易所止损",
    "TRAILING_STOP_LOSS": "跟踪止损",
    "STOP_LOSS": "止损",
    "ROI": "投资回报",
    "FORCE_EXIT": "强制退出",
    "FORCE_ENTRY": "强制进场",
    "EXIT_SIGNAL": "退出信号",
    "PARTIAL_EXIT": "部分退出",
    "PARTIAL_ADJUST": "部分调整",
    "EMERGENCY_EXIT": "紧急退出",
    "ENTRY_SIGNAL": "进场信号",
    "NONE": "无",
    "CANCELLED_ON_EXCHANGE": "交易所取消",
    "CANCELLED_ON_EXCHANGE_PARTIALLY": "交易所部分取消",
    "CANCELLED_ON_EXCHANGE_REPLACE": "交易所替换取消",
    "USER_CANCEL": "用户取消",
}
```

### freqtrade/freqtradebot.py

```python
# 状态通知
self.rpc.send_msg({
    "type": RPCMessageType.STATUS,
    "status": f"机器人已启动并同步中。使用 {self.state} 状态。"
})

# 警告消息
self.rpc.send_msg({
    "type": RPCMessageType.WARNING,
    "status": f"交易所不支持市价单。将使用限价单。"
})
```

### freqtrade/rpc/rpc_manager.py

```python
# 启动消息
self.send_msg({
    "type": RPCMessageType.STATUS,
    "status": f"正在启动 {len(self._active)} 个 RPC 模块。"
})

# 警告消息
self.send_msg({
    "type": RPCMessageType.WARNING,
    "status": f"无法启动 {name} 模块。"
})
```

## 如何恢复翻译

当 Freqtrade 版本更新后,您可以按照以下步骤恢复中文翻译：

1. 检查更新后的文件是否与原始文件结构相同
2. 对于每个文件,找到对应的方法或函数
3. 将上述中文翻译代码替换到相应的位置
4. 如果文件结构有变化,可能需要调整翻译代码以适应新的结构

注意：在恢复翻译时,请确保不要破坏代码的功能性。如果有疑问,可以先备份原始文件,然后再进行修改。

## 翻译文件列表

以下是所有已翻译的文件列表：

1. `freqtrade/rpc/telegram.py` - Telegram 消息翻译
2. `freqtrade/rpc/rpc.py` - RPC 状态消息翻译
3. `freqtrade/worker.py` - 工作者状态消息翻译
4. `freqtrade/enums/state.py` - 状态枚举翻译
5. `freqtrade/constants.py` - 取消订单原因翻译
6. `freqtrade/freqtradebot.py` - 机器人状态消息翻译
7. `freqtrade/rpc/rpc_manager.py` - RPC 管理器消息翻译
8. `freqtrade/plugins/pairlist/MarketCapPairList.py` - 市值配对列表描述翻译
9. `freqtrade/plugins/pairlist/RemotePairList.py` - 远程配对列表描述翻译
10. `freqtrade/plugins/pairlist/FullTradesFilter.py` - 全交易槽过滤器描述翻译
11. `freqtrade/plugins/pairlist/OffsetFilter.py` - 偏移过滤器描述翻译
12. `freqtrade/plugins/pairlist/ShuffleFilter.py` - 随机打乱过滤器描述翻译
13. `freqtrade/plugins/pairlist/PerformanceFilter.py` - 性能过滤器描述翻译
14. `freqtrade/plugins/pairlist/PercentChangePairList.py` - 百分比变化配对列表描述翻译
15. `freqtrade/plugins/pairlist/AgeFilter.py` - 年龄过滤器描述翻译
16. `freqtrade/plugins/pairlist/SpreadFilter.py` - 点差过滤器描述翻译
17. `freqtrade/plugins/pairlist/rangestabilityfilter.py` - 范围稳定性过滤器描述翻译
18. `freqtrade/plugins/pairlist/PrecisionFilter.py` - 精度过滤器描述翻译
19. `freqtrade/plugins/pairlist/VolatilityFilter.py` - 波动率过滤器描述翻译
20. `freqtrade/plugins/pairlist/VolumePairList.py` - 交易量配对列表描述翻译
21. `freqtrade/plugins/pairlist/PriceFilter.py` - 价格过滤器描述翻译
