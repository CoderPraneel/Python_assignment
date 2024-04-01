from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.cat = {}
        self.usr = {}
        self.trs = []

    def display_catalog(self):
        cat_info = "Catalog:\n"
        for b, i in self.cat.items():
            cat_info += f"ID: {b}, Title: {i['t']}, Author: {i['a']}, Available: {i['q']}\n"
        print(cat_info)

    def register_user(self, u, n):
        if u not in self.usr:
            self.usr[u] = {'n': n, 'bc': []}
            print(f"User '{n}' registered successfully with ID: {u}")
        else:
            print("User ID already exists. Please choose a different ID.")

    def checkout_book(self, u, b):
        if u not in self.usr:
            print("User ID not found. Please register first.")
            return
        if b not in self.cat:
            print("Book ID not found in catalog.")
            return
        if len(self.usr[u]['bc']) >= 3:
            print("Maximum limit of 3 books reached for this user.")
            return
        if self.cat[b]['q'] == 0:
            print("Book is not available for checkout.")
            return

        cd = datetime.now()
        dd = cd + timedelta(days=14)
        self.usr[u]['bc'].append({'b': b, 'cd': cd, 'dd': dd})
        self.cat[b]['q'] -= 1
        self.trs.append({'u': u, 'b': b, 'cd': cd})

        print(f"Book '{self.cat[b]['t']}' checked out successfully by user '{self.usr[u]['n']}'.")

    def return_book(self, u, b):
        if u not in self.usr:
            print("User ID not found. Please register first.")
            return
        if b not in self.cat:
            print("Book ID not found in catalog.")
            return

        for t in self.trs:
            if t['u'] == u and t['b'] == b:
                td = datetime.now()
                d_o = (td - t['cd']).days - 14
                if d_o > 0:
                    f = d_o
                    print(f"Book returned overdue by {d_o} days. Fine: ${f}.")
                else:
                    print("Book returned successfully.")
                self.cat[b]['q'] += 1
                self.usr[u]['bc'].remove({'b': b, 'cd': t['cd'], 'dd': t['cd'] + timedelta(days=14)})
                self.trs.remove(t)
                return
        print("Book was not checked out by this user.")

    def list_overdue_books(self, u):
        if u not in self.usr:
            print("User ID not found. Please register first.")
            return
        ob = []
        tf = 0
        for t in self.trs:
            if t['u'] == u:
                d_o = (datetime.now() - t['cd']).days - 14
                if d_o > 0:
                    ob.append({'b': t['b'], 'd_o': d_o})
                    tf += d_o
        if ob:
            ob_info = "Overdue Books:\n"
            for b in ob:
                ob_info += f"Book ID: {b['b']}, Days Overdue: {b['d_o']}\n"
            ob_info += f"Total Fine: ${tf}\n"
            print(ob_info)
        else:
            print("No overdue books for this user.")

