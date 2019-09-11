import pymongo
import xlwt


def client_mongo():
    try:
        # 连接mongo
        client = pymongo.MongoClient("localhost", 27017)

        # 连接数据库
        db = client.amazon

        # 获取集合
        collection = db['tws']

        # 查找所有
        cursor = collection.find({}, {'_id': 0})

        return cursor

    except Exception as e:
        print(e)


def save_to_excel():
    print("存储Excel")
    datas = client_mongo()
    try:
        # 创建工作workbook
        workbook = xlwt.Workbook(encoding="utf-8")

        # 创建工作表worksheet,填入表名
        worksheet = workbook.add_sheet('sheet1')

        worksheet.write(0, 0, '商品名称')
        worksheet.write(0, 1, '商品价格')
        worksheet.write(0, 2, '评价数量')
        worksheet.write(0, 3, '评价星级')
        worksheet.write(0, 4, '商品url')
        worksheet.write(0, 5, '类似商品')
        worksheet.write(0, 6, '排行')
        worksheet.write(0, 7, '商家')
        worksheet.write(0, 8, 'ASIN')
        worksheet.write(0, 9, '评论人1')
        worksheet.write(0, 10, '评论人星级1')
        worksheet.write(0, 11, '评论时间1')
        worksheet.write(0, 12, '评论内容1')
        worksheet.write(0, 13, '认同人数1')
        worksheet.write(0, 14, '评论人2')
        worksheet.write(0, 15, '评论人星级2')
        worksheet.write(0, 16, '评论时间2')
        worksheet.write(0, 17, '评论内容2')
        worksheet.write(0, 18, '认同人数2')
        worksheet.write(0, 19, '评论人3')
        worksheet.write(0, 20, '评论人星级3')
        worksheet.write(0, 21, '评论时间3')
        worksheet.write(0, 22, '评论内容3')
        worksheet.write(0, 23, '认同人数3')
        worksheet.write(0, 24, '评论人4')
        worksheet.write(0, 25, '评论人星级4')
        worksheet.write(0, 26, '评论时间4')
        worksheet.write(0, 27, '评论内容4')
        worksheet.write(0, 28, '认同人数4')

        # 在表中写入相应的数据
        a = 0
        for data in datas:
            c = 0
            a += 1
            # 1,0
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['price'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['commit'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['icon'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_url'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['upd'])
            c += 1
            worksheet.col(c).width = 256 * 30.
            worksheet.write(a, c, data['Bk'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['Mr'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['ASIN'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name1'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_icon1'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_time1'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_revie1'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_emen1'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name2'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_icon2'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_time2'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_revie2'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_emen2'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name3'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_icon3'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_time3'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_revie3'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_emen3'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name4'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_icon4'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_time4'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_revie4'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['name_emen4'])

            # 保存表
            workbook.save('TWS1.xls')
            print("存储Excel成功", a)

    except Exception as e:

        print("存储Excel失败", e)


def main():
    save_to_excel()


if __name__ == "__main__":
    main()
