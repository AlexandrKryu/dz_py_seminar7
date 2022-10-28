import view
import model


def run():
   exp = view.choice_calc()
   model.expression(exp)
   result = model.calc_exp()
   view.print_result(result)


