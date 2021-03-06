# Thanks to doronz88

from collections import namedtuple

irecv_device = namedtuple('irecv_device', 'product_type hardware_model bdid cpid display_name')

irecv_devices = (
    # iPhone
    irecv_device(product_type='iPhone1,1', hardware_model='m68ap', bdid=0x00, cpid=8900,
                display_name='iPhone 2G'),
    irecv_device(product_type='iPhone1,2', hardware_model='n82ap', bdid=0x04, cpid=8900,
                display_name='iPhone 3G'),
    irecv_device(product_type='iPhone2,1', hardware_model='n88ap', bdid=0x00, cpid=8920,
                display_name='iPhone 3Gs'),
    irecv_device(product_type='iPhone3,1', hardware_model='n90ap', bdid=0x00, cpid=8930,
                display_name='iPhone 4 (GSM)'),
    irecv_device(product_type='iPhone3,2', hardware_model='n90bap', bdid=0x04, cpid=8930,
                display_name='iPhone 4 (GSM) R2 2012'),
    irecv_device(product_type='iPhone3,3', hardware_model='n92ap', bdid=0x06, cpid=8930,
                display_name='iPhone 4 (CDMA)'),
    irecv_device(product_type='iPhone4,1', hardware_model='n94ap', bdid=0x08, cpid=8940,
                display_name='iPhone 4s'),
    irecv_device(product_type='iPhone5,1', hardware_model='n41ap', bdid=0x00, cpid=8950,
                display_name='iPhone 5 (GSM)'),
    irecv_device(product_type='iPhone5,2', hardware_model='n42ap', bdid=0x02, cpid=8950,
                display_name='iPhone 5 (Global)'),
    irecv_device(product_type='iPhone5,3', hardware_model='n48ap', bdid=0x0a, cpid=8950,
                display_name='iPhone 5c (GSM)'),
    irecv_device(product_type='iPhone5,4', hardware_model='n49ap', bdid=0x0e, cpid=8950,
                display_name='iPhone 5c (Global)'),
    irecv_device(product_type='iPhone6,1', hardware_model='n51ap', bdid=0x00, cpid=8960,
                display_name='iPhone 5s (GSM)'),
    irecv_device(product_type='iPhone6,2', hardware_model='n53ap', bdid=0x02, cpid=8960,
                display_name='iPhone 5s (Global)'),
    irecv_device(product_type='iPhone7,1', hardware_model='n56ap', bdid=0x04, cpid=7000,
                display_name='iPhone 6 Plus'),
    irecv_device(product_type='iPhone7,2', hardware_model='n61ap', bdid=0x06, cpid=7000,
                display_name='iPhone 6'),
    irecv_device(product_type='iPhone8,1', hardware_model='n71ap', bdid=0x04, cpid=8000,
                display_name='iPhone 6s'),
    irecv_device(product_type='iPhone8,1', hardware_model='n71map', bdid=0x04, cpid=8003,
                display_name='iPhone 6s'),
    irecv_device(product_type='iPhone8,2', hardware_model='n66ap', bdid=0x06, cpid=8000,
                display_name='iPhone 6s Plus'),
    irecv_device(product_type='iPhone8,2', hardware_model='n66map', bdid=0x06, cpid=8003,
                display_name='iPhone 6s Plus'),
    irecv_device(product_type='iPhone8,4', hardware_model='n69ap', bdid=0x02, cpid=8003,
                display_name='iPhone SE'),
    irecv_device(product_type='iPhone8,4', hardware_model='n69uap', bdid=0x02, cpid=8000,
                display_name='iPhone SE'),
    irecv_device(product_type='iPhone9,1', hardware_model='d10ap', bdid=0x08, cpid=8010,
                display_name='iPhone 7 (Global)'),
    irecv_device(product_type='iPhone9,2', hardware_model='d11ap', bdid=0x0a, cpid=8010,
                display_name='iPhone 7 Plus (Global)'),
    irecv_device(product_type='iPhone9,3', hardware_model='d101ap', bdid=0x0c, cpid=8010,
                display_name='iPhone 7 (GSM)'),
    irecv_device(product_type='iPhone9,4', hardware_model='d111ap', bdid=0x0e, cpid=8010,
                display_name='iPhone 7 Plus (GSM)'),
    irecv_device(product_type='iPhone10,1', hardware_model='d20ap', bdid=0x02, cpid=8015,
                display_name='iPhone 8 (Global)'),
    irecv_device(product_type='iPhone10,2', hardware_model='d21ap', bdid=0x04, cpid=8015,
                display_name='iPhone 8 Plus (Global)'),
    irecv_device(product_type='iPhone10,3', hardware_model='d22ap', bdid=0x06, cpid=8015,
                display_name='iPhone X (Global)'),
    irecv_device(product_type='iPhone10,4', hardware_model='d201ap', bdid=0x0a, cpid=8015,
                display_name='iPhone 8 (GSM)'),
    irecv_device(product_type='iPhone10,5', hardware_model='d211ap', bdid=0x0c, cpid=8015,
                display_name='iPhone 8 Plus (GSM)'),
    irecv_device(product_type='iPhone10,6', hardware_model='d221ap', bdid=0x0e, cpid=8015,
                display_name='iPhone X (GSM)'),
    irecv_device(product_type='iPhone11,2', hardware_model='d321ap', bdid=0x0e, cpid=8020,
                display_name='iPhone XS'),
    irecv_device(product_type='iPhone11,4', hardware_model='d331ap', bdid=0x0a, cpid=8020,
                display_name='iPhone XS Max (China)'),
    irecv_device(product_type='iPhone11,6', hardware_model='d331pap', bdid=0x1a, cpid=8020,
                display_name='iPhone XS Max'),
    irecv_device(product_type='iPhone11,8', hardware_model='n841ap', bdid=0x0c, cpid=8020,
                display_name='iPhone XR'),
    irecv_device(product_type='iPhone12,1', hardware_model='n104ap', bdid=0x04, cpid=8030,
                display_name='iPhone 11'),
    irecv_device(product_type='iPhone12,3', hardware_model='d421ap', bdid=0x06, cpid=8030,
                display_name='iPhone 11 Pro'),
    irecv_device(product_type='iPhone12,5', hardware_model='d431ap', bdid=0x02, cpid=8030,
                display_name='iPhone 11 Pro Max'),
    irecv_device(product_type='iPhone12,8', hardware_model='d79ap', bdid=0x10, cpid=8030,
                display_name='iPhone SE (2020)'),
    irecv_device(product_type='iPhone13,1', hardware_model='d52gap', bdid=0x0A, cpid=8101,
                display_name='iPhone 12 mini'),
    irecv_device(product_type='iPhone13,2', hardware_model='d53gap', bdid=0x0C, cpid=8101,
                display_name='iPhone 12'),
    irecv_device(product_type='iPhone13,3', hardware_model='d53pap', bdid=0x0E, cpid=8101,
                display_name='iPhone 12 Pro'),
    irecv_device(product_type='iPhone13,4', hardware_model='d54pap', bdid=0x08, cpid=8101,
                display_name='iPhone 12 Pro Max'),
    irecv_device(product_type='iPhone14,2', hardware_model='d63ap', bdid=0x0C, cpid=8110,
                display_name='iPhone 13 Pro'),
    irecv_device(product_type='iPhone14,3', hardware_model='d64ap', bdid=0x0E, cpid=8110,
                display_name='iPhone 13 Pro Max'),
    irecv_device(product_type='iPhone14,4', hardware_model='d16ap', bdid=0x08, cpid=8110,
                display_name='iPhone 13 mini'),
    irecv_device(product_type='iPhone14,5', hardware_model='d17ap', bdid=0x0A, cpid=8110,
                display_name='iPhone 13'),
    # iPod
    irecv_device(product_type='iPod1,1', hardware_model='n45ap', bdid=0x02, cpid=8900,
                display_name='iPod Touch (1st gen)'),
    irecv_device(product_type='iPod2,1', hardware_model='n72ap', bdid=0x00, cpid=8720,
                display_name='iPod Touch (2nd gen)'),
    irecv_device(product_type='iPod3,1', hardware_model='n18ap', bdid=0x02, cpid=8922,
                display_name='iPod Touch (3rd gen)'),
    irecv_device(product_type='iPod4,1', hardware_model='n81ap', bdid=0x08, cpid=8930,
                display_name='iPod Touch (4th gen)'),
    irecv_device(product_type='iPod5,1', hardware_model='n78ap', bdid=0x00, cpid=8942,
                display_name='iPod Touch (5th gen)'),
    irecv_device(product_type='iPod7,1', hardware_model='n102ap', bdid=0x10, cpid=7000,
                display_name='iPod Touch (6th gen)'),
    irecv_device(product_type='iPod9,1', hardware_model='n112ap', bdid=0x16, cpid=8010,
                display_name='iPod Touch (7th gen)'),
    # iPad
    irecv_device(product_type='iPad1,1', hardware_model='k48ap', bdid=0x02, cpid=8930, display_name='iPad'),
    irecv_device(product_type='iPad2,1', hardware_model='k93ap', bdid=0x04, cpid=8940,
                display_name='iPad 2 (WiFi)'),
    irecv_device(product_type='iPad2,2', hardware_model='k94ap', bdid=0x06, cpid=8940,
                display_name='iPad 2 (GSM)'),
    irecv_device(product_type='iPad2,3', hardware_model='k95ap', bdid=0x02, cpid=8940,
                display_name='iPad 2 (CDMA)'),
    irecv_device(product_type='iPad2,4', hardware_model='k93aap', bdid=0x06, cpid=8942,
                display_name='iPad 2 (WiFi) R2 2012'),
    irecv_device(product_type='iPad2,5', hardware_model='p105ap', bdid=0x0a, cpid=8942,
                display_name='iPad mini (WiFi)'),
    irecv_device(product_type='iPad2,6', hardware_model='p106ap', bdid=0x0c, cpid=8942,
                display_name='iPad mini (GSM)'),
    irecv_device(product_type='iPad2,7', hardware_model='p107ap', bdid=0x0e, cpid=8942,
                display_name='iPad mini (Global)'),
    irecv_device(product_type='iPad3,1', hardware_model='j1ap', bdid=0x00, cpid=8945,
                display_name='iPad (3rd gen, WiFi)'),
    irecv_device(product_type='iPad3,2', hardware_model='j2ap', bdid=0x02, cpid=8945,
                display_name='iPad (3rd gen, CDMA)'),
    irecv_device(product_type='iPad3,3', hardware_model='j2aap', bdid=0x04, cpid=8945,
                display_name='iPad (3rd gen, GSM)'),
    irecv_device(product_type='iPad3,4', hardware_model='p101ap', bdid=0x00, cpid=8955,
                display_name='iPad (4th gen, WiFi)'),
    irecv_device(product_type='iPad3,5', hardware_model='p102ap', bdid=0x02, cpid=8955,
                display_name='iPad (4th gen, GSM)'),
    irecv_device(product_type='iPad3,6', hardware_model='p103ap', bdid=0x04, cpid=8955,
                display_name='iPad (4th gen, Global)'),
    irecv_device(product_type='iPad4,1', hardware_model='j71ap', bdid=0x10, cpid=8960,
                display_name='iPad Air (WiFi)'),
    irecv_device(product_type='iPad4,2', hardware_model='j72ap', bdid=0x12, cpid=8960,
                display_name='iPad Air (Cellular)'),
    irecv_device(product_type='iPad4,3', hardware_model='j73ap', bdid=0x14, cpid=8960,
                display_name='iPad Air (China)'),
    irecv_device(product_type='iPad4,4', hardware_model='j85ap', bdid=0x0a, cpid=8960,
                display_name='iPad mini 2 (WiFi)'),
    irecv_device(product_type='iPad4,5', hardware_model='j86ap', bdid=0x0c, cpid=8960,
                display_name='iPad mini 2 (Cellular)'),
    irecv_device(product_type='iPad4,6', hardware_model='j87ap', bdid=0x0e, cpid=8960,
                display_name='iPad mini 2 (China)'),
    irecv_device(product_type='iPad4,7', hardware_model='j85map', bdid=0x32, cpid=8960,
                display_name='iPad mini 3 (WiFi)'),
    irecv_device(product_type='iPad4,8', hardware_model='j86map', bdid=0x34, cpid=8960,
                display_name='iPad mini 3 (Cellular)'),
    irecv_device(product_type='iPad4,9', hardware_model='j87map', bdid=0x36, cpid=8960,
                display_name='iPad mini 3 (China)'),
    irecv_device(product_type='iPad5,1', hardware_model='j96ap', bdid=0x08, cpid=7000,
                display_name='iPad mini 4 (WiFi)'),
    irecv_device(product_type='iPad5,2', hardware_model='j97ap', bdid=0x0A, cpid=7000,
                display_name='iPad mini 4 (Cellular)'),
    irecv_device(product_type='iPad5,3', hardware_model='j81ap', bdid=0x06, cpid=7001,
                display_name='iPad Air 2 (WiFi)'),
    irecv_device(product_type='iPad5,4', hardware_model='j82ap', bdid=0x02, cpid=7001,
                display_name='iPad Air 2 (Cellular)'),
    irecv_device(product_type='iPad6,3', hardware_model='j127ap', bdid=0x08, cpid=8001,
                display_name='iPad Pro 9.7-inch (WiFi)'),
    irecv_device(product_type='iPad6,4', hardware_model='j128ap', bdid=0x0a, cpid=8001,
                display_name='iPad Pro 9.7-inch (Cellular)'),
    irecv_device(product_type='iPad6,7', hardware_model='j98aap', bdid=0x10, cpid=8001,
                display_name='iPad Pro 12.9-inch (1st gen, WiFi)'),
    irecv_device(product_type='iPad6,8', hardware_model='j99aap', bdid=0x12, cpid=8001,
                display_name='iPad Pro 12.9-inch (1st gen, Cellular)'),
    irecv_device(product_type='iPad6,11', hardware_model='j71sap', bdid=0x10, cpid=8000,
                display_name='iPad (5th gen, WiFi)'),
    irecv_device(product_type='iPad6,11', hardware_model='j71tap', bdid=0x10, cpid=8003,
                display_name='iPad (5th gen, WiFi)'),
    irecv_device(product_type='iPad6,12', hardware_model='j72sap', bdid=0x12, cpid=8000,
                display_name='iPad (5th gen, Cellular)'),
    irecv_device(product_type='iPad6,12', hardware_model='j72tap', bdid=0x12, cpid=8003,
                display_name='iPad (5th gen, Cellular)'),
    irecv_device(product_type='iPad7,1', hardware_model='j120ap', bdid=0x0C, cpid=8011,
                display_name='iPad Pro 12.9-inch (2nd gen, WiFi)'),
    irecv_device(product_type='iPad7,2', hardware_model='j121ap', bdid=0x0E, cpid=8011,
                display_name='iPad Pro 12.9-inch (2nd gen, Cellular)'),
    irecv_device(product_type='iPad7,3', hardware_model='j207ap', bdid=0x04, cpid=8011,
                display_name='iPad Pro 10.5-inch (WiFi)'),
    irecv_device(product_type='iPad7,4', hardware_model='j208ap', bdid=0x06, cpid=8011,
                display_name='iPad Pro 10.5-inch (Cellular)'),
    irecv_device(product_type='iPad7,5', hardware_model='j71bap', bdid=0x18, cpid=8010,
                display_name='iPad (6th gen, WiFi)'),
    irecv_device(product_type='iPad7,6', hardware_model='j72bap', bdid=0x1A, cpid=8010,
                display_name='iPad (6th gen, Cellular)'),
    irecv_device(product_type='iPad7,11', hardware_model='j171ap', bdid=0x1C, cpid=8010,
                display_name='iPad (7th gen, WiFi)'),
    irecv_device(product_type='iPad7,12', hardware_model='j172ap', bdid=0x1E, cpid=8010,
                display_name='iPad (7th gen, Cellular)'),
    irecv_device(product_type='iPad8,1', hardware_model='j317ap', bdid=0x0C, cpid=8027,
                display_name='iPad Pro 11-inch (1st gen, WiFi)'),
    irecv_device(product_type='iPad8,2', hardware_model='j317xap', bdid=0x1C, cpid=8027,
                display_name='iPad Pro 11-inch (1st gen, WiFi, 1TB)'),
    irecv_device(product_type='iPad8,3', hardware_model='j318ap', bdid=0x0E, cpid=8027,
                display_name='iPad Pro 11-inch (1st gen, Cellular)'),
    irecv_device(product_type='iPad8,4', hardware_model='j318xap', bdid=0x1E, cpid=8027,
                display_name='iPad Pro 11-inch (1st gen, Cellular, 1TB)'),
    irecv_device(product_type='iPad8,5', hardware_model='j320ap', bdid=0x08, cpid=8027,
                display_name='iPad Pro 12.9-inch (3rd gen, WiFi)'),
    irecv_device(product_type='iPad8,6', hardware_model='j320xap', bdid=0x18, cpid=8027,
                display_name='iPad Pro 12.9-inch (3rd gen, WiFi, 1TB)'),
    irecv_device(product_type='iPad8,7', hardware_model='j321ap', bdid=0x0A, cpid=8027,
                display_name='iPad Pro 12.9-inch (3rd gen, Cellular)'),
    irecv_device(product_type='iPad8,8', hardware_model='j321xap', bdid=0x1A, cpid=8027,
                display_name='iPad Pro 12.9-inch (3rd gen, Cellular, 1TB)'),
    irecv_device(product_type='iPad8,9', hardware_model='j417ap', bdid=0x3C, cpid=8027,
                display_name='iPad Pro 11-inch (2nd gen, WiFi)'),
    irecv_device(product_type='iPad8,10', hardware_model='j418ap', bdid=0x3E, cpid=8027,
                display_name='iPad Pro 11-inch (2nd gen, Cellular)'),
    irecv_device(product_type='iPad8,11', hardware_model='j420ap', bdid=0x38, cpid=8027,
                display_name='iPad Pro 12.9-inch (4th gen, WiFi)'),
    irecv_device(product_type='iPad8,12', hardware_model='j421ap', bdid=0x3A, cpid=8027,
                display_name='iPad Pro 12.9-inch (4th gen, Cellular)'),
    irecv_device(product_type='iPad11,1', hardware_model='j210ap', bdid=0x14, cpid=8020,
                display_name='iPad mini (5th gen, WiFi)'),
    irecv_device(product_type='iPad11,2', hardware_model='j211ap', bdid=0x16, cpid=8020,
                display_name='iPad mini (5th gen, Cellular)'),
    irecv_device(product_type='iPad11,3', hardware_model='j217ap', bdid=0x1C, cpid=8020,
                display_name='iPad Air (3rd gen, WiFi)'),
    irecv_device(product_type='iPad11,4', hardware_model='j218ap', bdid=0x1E, cpid=8020,
                display_name='iPad Air (3rd gen, Celluar)'),
    irecv_device(product_type='iPad11,6', hardware_model='j171aap', bdid=0x24, cpid=8020,
                display_name='iPad (8th gen, WiFi)'),
    irecv_device(product_type='iPad11,7', hardware_model='j172aap', bdid=0x26, cpid=8020,
                display_name='iPad (8th gen, Cellular)'),
    irecv_device(product_type='iPad12,1', hardware_model='j181ap', bdid=0x18, cpid=8030,
                display_name='iPad (9th gen, WiFi)'),
    irecv_device(product_type='iPad12,2', hardware_model='j182ap', bdid=0x1A, cpid=8030,
                display_name='iPad (9th gen, Cellular)'),
    irecv_device(product_type='iPad13,1', hardware_model='j307ap', bdid=0x04, cpid=8101,
                display_name='iPad Air (4th gen, WiFi)'),
    irecv_device(product_type='iPad13,2', hardware_model='j308ap', bdid=0x06, cpid=8101,
                display_name='iPad Air (4th gen, Celluar)'),
    irecv_device(product_type='iPad13,4', hardware_model='j517ap', bdid=0x08, cpid=8103,
                display_name='iPad Pro 11-inch (3rd gen, WiFi)'),
    irecv_device(product_type='iPad13,5', hardware_model='j517xap', bdid=0x0A, cpid=8103,
                display_name='iPad Pro 11-inch (3rd gen, WiFi, 2TB)'),
    irecv_device(product_type='iPad13,6', hardware_model='j518ap', bdid=0x0C, cpid=8103,
                display_name='iPad Pro 11-inch (3rd gen, Cellular)'),
    irecv_device(product_type='iPad13,7', hardware_model='j518xap', bdid=0x0E, cpid=8103,
                display_name='iPad Pro 11-inch (3rd gen, Cellular, 2TB)'),
    irecv_device(product_type='iPad13,8', hardware_model='j522ap', bdid=0x18, cpid=8103,
                display_name='iPad Pro 12.9-inch (5th gen, WiFi)'),
    irecv_device(product_type='iPad13,9', hardware_model='j522xap', bdid=0x1A, cpid=8103,
                display_name='iPad Pro 12.9-inch (5th gen, WiFi, 2TB)'),
    irecv_device(product_type='iPad13,10', hardware_model='j523ap', bdid=0x1C, cpid=8103,
                display_name='iPad Pro 12.9-inch (5th gen, Cellular)'),
    irecv_device(product_type='iPad13,11', hardware_model='j523xap', bdid=0x1E, cpid=8103,
                display_name='iPad Pro 12.9-inch (5th gen, Cellular, 2TB)'),
    irecv_device(product_type='iPad14,1', hardware_model='j310ap', bdid=0x04, cpid=8110,
                display_name='iPad mini (6th gen, WiFi)'),
    irecv_device(product_type='iPad14,2', hardware_model='j311ap', bdid=0x06, cpid=8110,
                display_name='iPad mini (6th gen, Cellular)'),
    # Apple TV
    irecv_device(product_type='AppleTV2,1', hardware_model='k66ap', bdid=0x10, cpid=8930,
                display_name='Apple TV 2'),
    irecv_device(product_type='AppleTV3,1', hardware_model='j33ap', bdid=0x08, cpid=8942,
                display_name='Apple TV 3'),
    irecv_device(product_type='AppleTV3,2', hardware_model='j33iap', bdid=0x00, cpid=8947,
                display_name='Apple TV 3 (2013)'),
    irecv_device(product_type='AppleTV5,3', hardware_model='j42dap', bdid=0x34, cpid=7000,
                display_name='Apple TV 4'),
    irecv_device(product_type='AppleTV6,2', hardware_model='j105aap', bdid=0x02, cpid=8011,
                display_name='Apple TV 4K'),
    irecv_device(product_type='AppleTV11,1', hardware_model='j305ap', bdid=0x08, cpid=8020,
                display_name='Apple TV 4K (2nd gen)'),
    # HomePod
    irecv_device(product_type='AudioAccessory1,1', hardware_model='b238aap', bdid=0x38, cpid=7000,
                display_name='HomePod'),
    irecv_device(product_type='AudioAccessory1,2', hardware_model='b238ap', bdid=0x1A, cpid=7000,
                display_name='HomePod'),
    irecv_device(product_type='AudioAccessory5,1', hardware_model='b520ap', bdid=0x22, cpid=8006,
                display_name='HomePod mini'),
    # Apple Watch
    irecv_device(product_type='Watch1,1', hardware_model='n27aap', bdid=0x02, cpid=7002,
                display_name='Apple Watch 38mm (1st gen)'),
    irecv_device(product_type='Watch1,2', hardware_model='n28aap', bdid=0x04, cpid=7002,
                display_name='Apple Watch 42mm (1st gen)'),
    irecv_device(product_type='Watch2,6', hardware_model='n27dap', bdid=0x02, cpid=8002,
                display_name='Apple Watch Series 1 (38mm)'),
    irecv_device(product_type='Watch2,7', hardware_model='n28dap', bdid=0x04, cpid=8002,
                display_name='Apple Watch Series 1 (42mm)'),
    irecv_device(product_type='Watch2,3', hardware_model='n74ap', bdid=0x0C, cpid=8002,
                display_name='Apple Watch Series 2 (38mm)'),
    irecv_device(product_type='Watch2,4', hardware_model='n75ap', bdid=0x0E, cpid=8002,
                display_name='Apple Watch Series 2 (42mm)'),
    irecv_device(product_type='Watch3,1', hardware_model='n111sap', bdid=0x1C, cpid=8004,
                display_name='Apple Watch Series 3 (38mm Cellular)'),
    irecv_device(product_type='Watch3,2', hardware_model='n111bap', bdid=0x1E, cpid=8004,
                display_name='Apple Watch Series 3 (42mm Cellular)'),
    irecv_device(product_type='Watch3,3', hardware_model='n121sap', bdid=0x18, cpid=8004,
                display_name='Apple Watch Series 3 (38mm)'),
    irecv_device(product_type='Watch3,4', hardware_model='n121bap', bdid=0x1A, cpid=8004,
                display_name='Apple Watch Series 3 (42mm)'),
    irecv_device(product_type='Watch4,1', hardware_model='n131sap', bdid=0x08, cpid=8006,
                display_name='Apple Watch Series 4 (40mm)'),
    irecv_device(product_type='Watch4,2', hardware_model='n131bap', bdid=0x0A, cpid=8006,
                display_name='Apple Watch Series 4 (44mm)'),
    irecv_device(product_type='Watch4,3', hardware_model='n141sap', bdid=0x0C, cpid=8006,
                display_name='Apple Watch Series 4 (40mm Cellular)'),
    irecv_device(product_type='Watch4,4', hardware_model='n141bap', bdid=0x0E, cpid=8006,
                display_name='Apple Watch Series 4 (44mm Cellular)'),
    irecv_device(product_type='Watch5,1', hardware_model='n144sap', bdid=0x10, cpid=8006,
                display_name='Apple Watch Series 5 (40mm)'),
    irecv_device(product_type='Watch5,2', hardware_model='n144bap', bdid=0x12, cpid=8006,
                display_name='Apple Watch Series 5 (44mm)'),
    irecv_device(product_type='Watch5,3', hardware_model='n146sap', bdid=0x14, cpid=8006,
                display_name='Apple Watch Series 5 (40mm Cellular)'),
    irecv_device(product_type='Watch5,4', hardware_model='n146bap', bdid=0x16, cpid=8006,
                display_name='Apple Watch Series 5 (44mm Cellular)'),
    irecv_device(product_type='Watch5,9', hardware_model='n140sap', bdid=0x28, cpid=8006,
                display_name='Apple Watch SE (40mm)'),
    irecv_device(product_type='Watch5,10', hardware_model='n140bap', bdid=0x2A, cpid=8006,
                display_name='Apple Watch SE (44mm)'),
    irecv_device(product_type='Watch5,11', hardware_model='n142sap', bdid=0x2C, cpid=8006,
                display_name='Apple Watch SE (40mm Cellular)'),
    irecv_device(product_type='Watch5,12', hardware_model='n142bap', bdid=0x2E, cpid=8006,
                display_name='Apple Watch SE (44mm Cellular)'),
    irecv_device(product_type='Watch6,1', hardware_model='n157sap', bdid=0x08, cpid=8301,
                display_name='Apple Watch Series 6 (40mm)'),
    irecv_device(product_type='Watch6,2', hardware_model='n157bap', bdid=0x0A, cpid=8301,
                display_name='Apple Watch Series 6 (44mm)'),
    irecv_device(product_type='Watch6,3', hardware_model='n158sap', bdid=0x0C, cpid=8301,
                display_name='Apple Watch Series 6 (40mm Cellular)'),
    irecv_device(product_type='Watch6,4', hardware_model='n158bap', bdid=0x0E, cpid=8301,
                display_name='Apple Watch Series 6 (44mm Cellular)'),
    irecv_device(product_type='Watch6,6', hardware_model='n187sap', bdid=0x10, cpid=8301,
                display_name='Apple Watch Series 7 (41mm)'),
    irecv_device(product_type='Watch6,7', hardware_model='n187bap', bdid=0x12, cpid=8301,
                display_name='Apple Watch Series 7 (45mm)'),
    irecv_device(product_type='Watch6,8', hardware_model='n188sap', bdid=0x14, cpid=8301,
                display_name='Apple Watch Series 7 (41mm Cellular)'),
    irecv_device(product_type='Watch6,9', hardware_model='n188bap', bdid=0x16, cpid=8301,
                display_name='Apple Watch Series 7 (45mm Cellular)'),
    # Apple Silicon Macs
    irecv_device(product_type='ADP3,2', hardware_model='j273aap', bdid=0x42, cpid=8027,
                display_name='Developer Transition Kit (2020)'),
    irecv_device(product_type='Macmini9,1', hardware_model='j274ap', bdid=0x22, cpid=8103,
                display_name='Mac mini (M1, 2020)'),
    irecv_device(product_type='MacBookPro17,1', hardware_model='j293ap', bdid=0x24, cpid=8103,
                display_name='MacBook Pro (M1, 2020)'),
    irecv_device(product_type='MacBookPro18,1', hardware_model='j316sap', bdid=0x0A, cpid=6000,
                display_name='MacBook Pro (M1 Pro, 16-inch, 2021)'),
    irecv_device(product_type='MacBookPro18,2', hardware_model='j316cap', bdid=0x0A, cpid=6001,
                display_name='MacBook Pro (M1 Max, 16-inch, 2021)'),
    irecv_device(product_type='MacBookPro18,3', hardware_model='j314sap', bdid=0x08, cpid=6000,
                display_name='MacBook Pro (M1 Pro, 14-inch, 2021)'),
    irecv_device(product_type='MacBookPro18,4', hardware_model='j314cap', bdid=0x08, cpid=6001,
                display_name='MacBook Pro (M1 Max, 14-inch, 2021)'),
    irecv_device(product_type='MacBookAir10,1', hardware_model='j313ap', bdid=0x26, cpid=8103,
                display_name='MacBook Air (M1, 2020)'),
    irecv_device(product_type='iMac21,1', hardware_model='j456ap', bdid=0x28, cpid=8103,
                display_name='iMac 24-inch (M1, Two Ports, 2021)'),
    irecv_device(product_type='iMac21,2', hardware_model='j457ap', bdid=0x2A, cpid=8103,
                display_name='iMac 24-inch (M1, Four Ports, 2021)'),
    # Apple T2 Coprocessor
    irecv_device(product_type='iBridge2,1', hardware_model='j137ap', bdid=0x0A, cpid=8012,
                display_name='Apple T2 iMacPro1,1 (j137)'),
    irecv_device(product_type='iBridge2,3', hardware_model='j680ap', bdid=0x0B, cpid=8012,
                display_name='Apple T2 MacBookPro15,1 (j680)'),
    irecv_device(product_type='iBridge2,4', hardware_model='j132ap', bdid=0x0C, cpid=8012,
                display_name='Apple T2 MacBookPro15,2 (j132)'),
    irecv_device(product_type='iBridge2,5', hardware_model='j174ap', bdid=0x0E, cpid=8012,
                display_name='Apple T2 Macmini8,1 (j174)'),
    irecv_device(product_type='iBridge2,6', hardware_model='j160ap', bdid=0x0F, cpid=8012,
                display_name='Apple T2 MacPro7,1 (j160)'),
    irecv_device(product_type='iBridge2,7', hardware_model='j780ap', bdid=0x07, cpid=8012,
                display_name='Apple T2 MacBookPro15,3 (j780)'),
    irecv_device(product_type='iBridge2,8', hardware_model='j140kap', bdid=0x17, cpid=8012,
                display_name='Apple T2 MacBookAir8,1 (j140k)'),
    irecv_device(product_type='iBridge2,10', hardware_model='j213ap', bdid=0x18, cpid=8012,
                display_name='Apple T2 MacBookPro15,4 (j213)'),
    irecv_device(product_type='iBridge2,12', hardware_model='j140aap', bdid=0x37, cpid=8012,
                display_name='Apple T2 MacBookAir8,2 (j140a)'),
    irecv_device(product_type='iBridge2,14', hardware_model='j152fap', bdid=0x3A, cpid=8012,
                display_name='Apple T2 MacBookPro16,1 (j152f)'),
    irecv_device(product_type='iBridge2,15', hardware_model='j230kap', bdid=0x3F, cpid=8012,
                display_name='Apple T2 MacBookAir9,1 (j230k)'),
    irecv_device(product_type='iBridge2,16', hardware_model='j214kap', bdid=0x3E, cpid=8012,
                display_name='Apple T2 MacBookPro16,2 (j214k)'),
    irecv_device(product_type='iBridge2,19', hardware_model='j185ap', bdid=0x22, cpid=8012,
                display_name='Apple T2 iMac20,1 (j185)'),
    irecv_device(product_type='iBridge2,20', hardware_model='j185fap', bdid=0x23, cpid=8012,
                display_name='Apple T2 iMac20,2 (j185f)'),
    irecv_device(product_type='iBridge2,21', hardware_model='j223ap', bdid=0x3B, cpid=8012,
                display_name='Apple T2 MacBookPro16,3 (j223)'),
    irecv_device(product_type='iBridge2,22', hardware_model='j215ap', bdid=0x38, cpid=8012,
                display_name='Apple T2 MacBookPro16,4 (j215)'),
)