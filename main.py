from matplotlib import pyplot


def fit_linear(filename):
        pointer = open(filename, 'r')
        data = pointer.readlines()
        y_label = data[-1]
        x_label = data[-2]
        def graph(organized_data):
           data_points = len(organized_data[0])
           term1 = sum(1/organized_data["dx"] ^ 2)
           term3 = sum((organized_data["x"] ^ 2)/(organized_data["dx"] ^ 2))
           term4 = sum((organized_data["y"])/(organized_data["dy"] ^ 2))
           term5 = sum(organized_data["x"]*organized_data["y"]/(organized_data["dx"] ^2 *organized_data["dy"] ^ 2))
           term6 = sum((organized_data["x"])/(organized_data["dx"] ^ 2))
           delta = term1*term3-term6 ^ 2
           b = (term3*term4-term6*term5)/delta
           a = (term1*term5-term6*term4)/delta
           aerr = (term1/delta) ^ 0.5
           berr = (term3/delta) ^ 0.5
           chisq = sum(((organized_data["y"]-b-a*organized_data["x"])/(organized_data["dx"]+organized_data["dy"])) ^ 2)
           print("Evaluated fitting parameters:")
           print("a =", a, "+-", aerr)
           print("b =", b, "+-", berr)
           print("chi2 = ",chisq)
           print("chi2_reduced = ", chisq/(data_points-2))
           pyplot.plot(organized_data["x"], b+a*organized_data["x"],'r--')
           pyplot.errorbar(organized_data["x"],organized_data["y"],yerr= organized_data["dy"],xerr= organized_data,ecolor= 'b')
           pyplot.ylabel(y_label)
           pyplot.xlabel(x_label)
           pyplot.show()
           pyplot.savefig("linear_fit",format="svg")



        def columns(data_columns):
                helper_dictionary={}
                data_columns[0].lower()
                helper_list= data_columns[0].split(" ")
                x_index = helper_list.index("x")
                y_index = helper_list.index("y")
                dx_index = helper_list.index("dx")
                dy_index = helper_list.index("dy")
                for line in data_columns:
                        if line == data_columns[-2]:
                                break
                        if line == data_columns[0]:
                                continue
                        helper_list = line.split(" ")
                        helper_dictionary["x"].append(float(helper_list[x_index]))
                        helper_dictionary["y"].append(float(helper_list[y_index]))
                        helper_dictionary["dx"].append(float(helper_list[dx_index]))
                        helper_dictionary["dy"].append(float(helper_list[dy_index]))
                return helper_dictionary

        def rows(data_rows):
                helper_dictionary = {}
                for line in data_rows:
                        helper_list = line.split(" ")
                        helper_list[0].lower()
                        for count in range(1, len(helper_list)):
                                helper_list[count] = float(helper_list[count])

                        helper_dictionary[helper_list[0]].extend(helper_list, 1, len(helper_list))
                return helper_dictionary
        if ("y" or "Y") and ("x" or "X") in data[0]:
                       organized_data = columns(data)
        else:
                       organized_data = rows(data)
        if min(organized_data["dx"]) <= 0 or min(organized_data["dy"]) <= 0:
                print("Input file error: Not all uncertainties are positive")
        else:
                for count in range(0,3):
                        if len(organized_data[0])!=len(organized_data[count]):
                                print("Input file error: Data lists are not the same length")
                                break
                graph(organized_data)

       





