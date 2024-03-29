# ExpressionEvaluator

`ExpressionEvaluator` 是一个使用栈数据结构实现的算术表达式求值工具。

## 功能

- 输入算术表达式。
- 使用两个栈（算符栈 OPTR 和操作数栈 OPND）来求值。
- 显示计算结果。

## 使用方法

1. 在 Streamlit 应用中输入算术表达式。
2. 点击"求值"按钮。
3. 观察计算结果。

## 测试用例

以下是一些测试用例，您可以使用它们来验证工具的准确性：

1. `3+5` 结果应为 `8`
2. `12-5` 结果应为 `7`
3. `3*7` 结果应为 `21`
4. `8/2` 结果应为 `4`
5. `15+3*2` 结果应为 `21`
6. `8+12/4*3` 结果应为 `14`
7. `18/(3+3)*2` 结果应为 `6`

## 注意事项

- 当前版本仅支持整数计算。
- 请确保您的表达式格式正确，避免使用空格或其他非算术字符。
