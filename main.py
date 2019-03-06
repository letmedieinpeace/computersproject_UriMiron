from matplotlib import pyplot


def fit_linear(filename):
        pointer = open(filename, 'r')
        data = pointer.readlines()
        y_label = data[-1]
        x_label = data[-2]
        x_y_list = ["X", "x", "Y", "y"]
        headline_list = ["x", "y", "dx", "dy"]

        def graph(organized_data):
            data_points = len(organized_data["x"])

            dy_2 =[]
            dy2_denom_list =[]
            for k in organized_data["dy"]:   #to count using for loops, I will use the dummy interval k

                dy2_denom_list.append(1/ k**2)
                dy_2.append(k**2)
            dy2_denom = sum(dy2_denom_list)
            x_2 = []
            for k in organized_data["x"]:
                x_2.append(k**2)
            x_y = []
            for k in range(len(organized_data["x"])):
                x_y.append(organized_data["x"][k]*organized_data["y"][k])
            term1 = 0
            term2 = 0
            term3 = 0
            term4 = 0
            term5 = 0
            for k in range(data_points):
                term1 = term1 + organized_data["x"][k] * dy2_denom_list[k]
                term2 = term2 + organized_data["y"][k] * dy2_denom_list[k]
                term3 = term3 + x_y[k]*dy2_denom_list[k]
                term4 = term4 + x_2[k]*dy2_denom_list[k]
                term5 = term5 + dy_2[k]*dy2_denom_list[k]
            final_term_list = [term1/dy2_denom, term2/dy2_denom, term3/dy2_denom, term4/dy2_denom, term5/dy2_denom]
            a = (final_term_list[2]-(final_term_list[0]*final_term_list[1]))/(final_term_list[3]-final_term_list[0]**2)
            aerr = (final_term_list[4]/data_points*(final_term_list[3]-final_term_list[0]**2))**0.5
            b = final_term_list[1]-(a*final_term_list[0])
            berr = (final_term_list[4]*final_term_list[3]/data_points*(final_term_list[3]-final_term_list[0]**2))**0.5
            chisq = 0
            for k in range(data_points):
                d = organized_data["y"][k]-(a*organized_data["x"][k]+b)
                r = (d/organized_data["dy"][k])**2
                chisq = chisq + r
            line_y = []
            for k in range(data_points):
                line_y.append(organized_data["x"][k]*a+b)
            print("Evaluated fitting parameters:")
            print("a =", a, "+-", aerr)
            print("b =", b, "+-", berr)
            print("chi2 = ", chisq)
            print("chi2_reduced = ", chisq/(data_points-2))
            pyplot.plot(organized_data["x"], line_y, 'r--')
            pyplot.errorbar(organized_data["x"], organized_data["y"], yerr=organized_data["dy"], xerr=organized_data["dx"], ecolor='b')
            pyplot.ylabel(y_label)
            pyplot.xlabel(x_label)
            pyplot.show()
            pyplot.savefig("linear_fit", format="svg")
            pointer.close()


        def columns(data_columns):
                helper_dictionary = {}
                data_columns[0] = data_columns[0].lower()
                helper_list = data_columns[0].strip("\n").split(" ")
                x_index = helper_list.index("x")
                y_index = helper_list.index("y")
                dx_index = helper_list.index("dx")
                dy_index = helper_list.index("dy")
                x_values = []
                y_values = []
                dy_values = []
                dx_values = []
                for line in data_columns:
                    if line == data_columns[-3]:
                        break
                    if line == data_columns[0]:
                        continue
                    line = line.strip("\n").split(" ")
                    x_values.append(float(line[x_index]))
                    y_values.append(float(line[y_index]))
                    dy_values.append(float((line[dy_index])))
                    dx_values.append(float(line[dx_index]))
                helper_dictionary["x"] = x_values
                helper_dictionary["y"] = y_values
                helper_dictionary["dx"] = dx_values
                helper_dictionary["dy"] = dy_values
                return helper_dictionary

        def rows(data_rows):
                helper_dictionary = {}

                for line in data_rows:
                    values_list = []
                    if line == data_rows[-2]:
                        break
                    helper_list = line.strip("\n").split(" ")
                    helper_list[0] = helper_list[0].lower()
                    for k in range(1, len(helper_list)):
                            helper_list[k] = float(helper_list[k])
                            values_list.append(helper_list[k])
                    helper_dictionary[helper_list[0]] = values_list
                return helper_dictionary
        g = 0
        for k in range(len(x_y_list)):
            if x_y_list[k] in data[0]:
                g = g+1
        if g >= 2:
                       organized_data = columns(data)
        else:
                       organized_data = rows(data)
        if min(organized_data["dx"]) <= 0 or min(organized_data["dy"]) <= 0:
                print("Input file error: Not all uncertainties are positive")
        else:
                for k in headline_list:
                        if len(organized_data["x"]) != len(organized_data[k]):
                                print("Input file error: Data lists are not the same length")
                                break
                graph(organized_data)







