import cherrypy
import solver


class StringGenerator(object):
    @cherrypy.expose
    def index(self, equation="x + 1 = 0"):
        answer = None
        error = None
        if equation:
            try:
                answer = solver.solve(equation)
            except solver.NotLinearEquationError:
                error = "Your expression doesn't look like linear equation"

        result = "x = {}".format(answer) if answer is not None else error

        return """<html>
          <head></head>
          <body>
            <form method="get" action="index">
              <label>Linear equation:</label>
              <input type="text" value="{equation}" name="equation"/>
              <button type="submit">Solve!</button>
            </form>
            <div>{result}</div>
          </body>
        </html>
        """.format(equation=equation, result=result)

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
