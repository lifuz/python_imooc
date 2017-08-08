# coding:utf8
class HtmlOutputer(object):

    __datas = []

    def collect_data(self, data):
        if data is None:
            return
        HtmlOutputer.__datas.append(data)

    def output_html(self):
        fout = open('output.html','w',encoding='utf-8')

        fout.write('<!DOCTYPE html>')
        fout.write('<html lang="en">')
        fout.write('<head>')
        fout.write('<meta charset="UTF-8">')
        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
        fout.write('<title>爬取结果</title>')
        fout.write('</head>')
        fout.write('<body>')

        fout.write('<table>')

        for res_data in HtmlOutputer.__datas:
            fout.write('<tr>')

            fout.write('<td>%s</td>' % res_data['url'])
            fout.write('<td>%s</td>' % res_data['title'])
            fout.write('<td>%s</td>' % res_data['summary'])

            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()