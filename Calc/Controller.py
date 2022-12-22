import View
import Model
import Logger


def run():
    # while True:
    turn = View.choose()
    if turn == '1':
        expression = View.get_expr()
        result = Model.execute_expr(expression)
        View.show_result(result)
        Logger.log_exec(expression, result)
    elif turn == '2':
        expression = View.get_expr()
        result = Model.solve_eq(expression)
        View.show_result(result)
        Logger.log_exec(expression, result)
    elif turn == '3':
        expression = View.get_expr()
        result = Model.simple(expression)
        View.show_result(result)
        Logger.log_exec(expression, result)
    elif turn == '4':
        history = Logger.get_history()
        View.show_history(history)
    else:
        View.error_mode()
