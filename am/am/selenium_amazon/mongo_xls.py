import pymongo
import xlwt


def client_mongo():
    try:
        # 连接mongo
        client = pymongo.MongoClient("localhost", 27017)

        # 连接数据库
        db = client.amazon

        # 获取集合
        collection = db['Headphones']

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
        worksheet.write(0, 5, 'ASIN码')
        worksheet.write(0, 6, '排行1')
        worksheet.write(0, 7, '排行2')
        worksheet.write(0, 8, '店家名称')
        worksheet.write(0, 9, '包装尺寸')
        worksheet.write(0, 10, '重量')
        worksheet.write(0, 11, '起价')

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
            worksheet.write(a, c, data['ASIN'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['BestSellersRank1'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['BestSellersRank2'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['Manufacturer'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['PackageDimensions'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['ItemWeight'])
            c += 1
            worksheet.col(c).width = 256 * 30
            worksheet.write(a, c, data['upd'])

            # 保存表
            # workbook.save('Accesorios_PO94LJ.xls')
            workbook.save('TWS.xls')
            # workbook.save('Accesorios_10010.xls')
            print("存储Excel成功", a)

    except Exception:

        print("存储Excel失败")


def main():
    save_to_excel()


if __name__ == "__main__":
    main()
