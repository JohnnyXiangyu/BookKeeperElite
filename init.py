import web
import modules.book as book
import modules.utils.configure as configs

# TODO: implement server part
# render = web.template.render('templates/')

# urls = (
#     '/(.*)', 'index'
# )

# class index:
#     def GET(self, name):
#         return render.home(name)


# if __name__ == "__main__":
#     app = web.application(urls, globals())
#     app.run()

# TODO: implement database

# book.mkBook('testbook.db', 'dummy2', {"dummyline": "INT", "dummycircle": "REAL"}, 'this is a dummy book in db')

print(configs.getTuesdaySchema())

print('testpass')
