
"""
data = {
    storeCategory: '库存第三级的objectId',
    saleCategory: ['销售的第二级objectId'],
    name: 'name',
    briefDescription: 'briefDescription',
    mainImage: src data,
    imageList: ['data','data'],
    spec: [
        {
            'SpecName': 'spec',
            'SpecContent': 'specText'
        }
    ],
    productService: ['objectId', 'objcetId'],
    detailDescription: ['data','data'],
    
    
    propertyOption: '[
    {
        "PropertyId":"0","PropertyName":"颜色",
        "PropertyOption":
            [{"OptionId":"0","OptionName":"红色"},
            {"OptionId":"1","OptionName":"黄色"}
            ]
        },
    {"PropertyId":"1",
    "PropertyName":"大小",
    "PropertyOption":
        [
            {   "OptionId":"0",
                "OptionName":"大号"
                },
                {"OptionId":"1",
                "OptionName":"小号"}
                ]
            }
        ]',
    

    product: '[
    {
        "style":[
            {"PropertyId":"0",
            "OptionId":"0"},
            {"PropertyId":"1",
            "OptionId":"0"}
        ],
        "price":"1",
        "stockCount":"22",
        "mainImage":""
    },
        
    {"style":
        [
        {"PropertyId":"0",
        "OptionId":"1"},
        {"PropertyId":"1",
        "OptionId":"1"
        }
        ],
        "price":"11",
        "stockCount":"22",
        "mainImage":""}
    ]',

    delete_imageList: 'delete_imageList',
    delte_product: 'delete_product',
    delete_detailDescription: 'delete_detailDescription',
} 
"""