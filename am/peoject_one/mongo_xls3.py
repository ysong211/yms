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
        worksheet.write(0, 0, '评论人')
        worksheet.write(0, 1, '评论人星级')
        worksheet.write(0, 2, '评论时间')
        worksheet.write(0, 3, '评论内容')
        worksheet.write(0, 4, '认同人数')
        worksheet.write(0, 5, '评论人链接')
        worksheet.write(0, 6, 'ASIN')
        worksheet.write(0, 7, '商品名称')
        worksheet.write(0, 8, '排名')
        worksheet.write(0, 9, '商家')
        worksheet.write(0, 10, '商品价格')
        worksheet.write(0, 11, '评价数量')
        worksheet.write(0, 12, '评价星级')
        worksheet.write(0, 13, '商品url')


        # 在表中写入相应的数据
        a = 0
        for data in datas:
            for i in range(1, 5):
                c = 0
                a += 1
                name = "name" + str(i)
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data[name])
                c += 1
                name = "name_icon" + str(i)
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data[name])
                c += 1
                name = "name_time" + str(i)
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data[name])
                c += 1
                name = "name_revie" + str(i)
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data[name])
                c += 1
                name = "name_emen" + str(i)
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data[name])
                c += 1
                name = "name_like" + str(i)
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data[name])
                c += 1
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data['ASIN'])
                c += 1
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data['name'])
                c += 1
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data['Bk'])
                c += 1
                worksheet.col(c).width = 256 * 30
                worksheet.write(a, c, data['Mr'])
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

                # 保存表
                workbook.save('TWS2.xls')
                print("存储Excel成功", a)

    except Exception as e:

        print("存储Excel失败", e)


def main():
    save_to_excel()


if __name__ == "__main__":
    main()
