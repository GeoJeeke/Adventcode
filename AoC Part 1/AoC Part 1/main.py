class Main(object):
    def texttofile(self):
        a_dictionary = {}
        myfile = open("inputone.txt", "r")
        myline = myfile.readline()
        i = 1

        for line in myfile:
            if not line.strip() == "":
                a_dictionary.setdefault(i, []).append(int(line))
            else:
                i = i + 1
        myfile.close()
        return a_dictionary

    def summerize_dict(self,a_dictionary):
        sum_dic = {}
        o = 0
        total = len(a_dictionary)
        while total > 0:
            o = o + 1
            sum_dic[o] = sum(a_dictionary[o])
            total = total - 1
        max_value = max(sum_dic.values())
        return max_value,sum_dic


    def sorting_dict(self,sum_dic):
        #Sort dict
        return dict(sorted(sum_dic.items(), key=lambda x: x[1], reverse=True))

    def get_dict_val(self,a_dict):
        first3pairs = {k: a_dict[k] for k in list(a_dict)[:3]}
        sumpar = sum(first3pairs.values())
        print(sumpar)

if __name__ == '__main__':
    start = Main()
    conv_dict = start.texttofile()
    max_value,sum_dic = start.summerize_dict(conv_dict)
    sorted_dict = start.sorting_dict(sum_dic)
    start.get_dict_val(sorted_dict)

