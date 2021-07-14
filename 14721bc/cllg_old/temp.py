sudo mount.cifs //192.168.0.160/shared /home/pi/Desktop/thegamechanger -o user=kasppr,pass=prat1112



df['str_list'] = df.apply(lambda row: ' '.join([str(int(val)) for val in row]), axis=1)
df8 = pd.DataFrame(df9['str_list'].value_counts().values, index=df9['str_list'].value_counts().index, columns=['Count'])

sdf = df2[df2['Site'] == 'SK MINES'][df2['Equipment_Type'] == 'EN'][df2['MODEL'] == 'TH-663']


    # this method returns the corrected string of the given input
def correct(self):
        # store the words of the string to be checked in a list by using a split function
    string_words = self.string_to_check.split()

        # loop over the number of words in the string to be checked
    for i in range(len(string_words)):

            # initiaze a maximum probability variable to 0
        max_percent = 0

            # loop over the words in the dictionary
        for name in self.dictionary:

                # calulcate the match probability
            percent = fuzz.ratio(string_words[i].lower(), name.lower())

                # if the fuzzywuzzy returns the matched value greater than 80
            if percent >= 75:

                    # if the matched probability is
                if percent > max_percent:

                        # change the original value with the corrected matched value
                    string_words[i] = name

                    # change the max percent to the current matched percent
                max_percent = percent

        # return the cprrected string
    return " ".join(string_words)
