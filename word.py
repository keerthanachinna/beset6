num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             def n2w(n):
        try:
            print num2words[n]
        except KeyError:
            try:
                print num2words[n-n%10] + num2words[n%10].lower()
            except KeyError:
                print 'Number out of range'
                n2w(1)
