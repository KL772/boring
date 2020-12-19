'''
Training data recieved from the COMSOL model

Author: Dustin Hall, Jeff Chin
'''

import numpy as np
import openmdao.api as om

t_data = np.array([

    [   # extra_data = 1.0
    [293.15,  293.2984739, 295.33441,   302.4282878, 314.473288,  327.708266,  340.3190001, 351.1479065, 359.7873155, 366.3050094, 371.0518968, 374.4682527, 376.9879232, 378.9879599, 380.3841539, 381.5575116, 382.5522994, 383.5081202, 384.463941,  385.3365905, 386.1226754, 386.9087602, 387.6948451, 388.48093,   389.2670148, 389.9976113, 390.6704556, 391.3432999, 392.0161441, 392.6889884, 393.3618327, 393.9896324, 394.5705497, 395.1514671, 395.7323844, 396.3133018, 396.8942191, 397.4601476, 398.0034528, 398.5373314, 399.0617834, 399.5768088, 400.0824076, 400.5757985, 401.0555647, 401.5241552, 401.9815698, 402.4278087, 402.8628717, 403.2864943, 403.6985416, 404.0992467, 404.4886095, 404.8666301, 405.2333085, 405.5899426, 405.9371934, 406.2739183, 406.6001173, 406.9157902, 407.2209373],
    [293.15,  293.9156189, 300.0807259, 314.2552988, 331.0516796, 345.8578117, 357.8917187, 366.8998106, 373.3455933, 377.8535182, 381.021119,  383.3343673, 385.1258972, 386.6317513, 387.7533163, 388.7768558, 389.8003953, 390.7797668, 391.6848522, 392.5899376, 393.4824301, 394.2514747, 395.0205193, 395.789564,  396.5586086, 397.3276532, 398.0862848, 398.7428382, 399.3993916, 400.055945,  400.7124984, 401.3690518, 402.0165374, 402.5751324, 403.1337275, 403.6923225, 404.2509176, 404.8095126, 405.3652403, 405.8873051, 406.3992015, 406.9009297, 407.3924895, 407.8738811, 408.3445725, 408.7988522, 409.2410777, 409.671249,  410.0893661, 410.4954289, 410.8894036, 411.2709252, 411.640272,  411.9974441, 412.3424416, 412.6752643, 412.9961867, 413.3081561, 413.6089239, 413.8984902, 414.1768549],
    [293.15,  294.7692893, 304.7245591, 323.0915891, 341.6221493, 357.2232293, 369.1941077, 377.8792359, 383.9934231, 388.2907259, 391.4016012, 393.8004728, 395.8061419, 397.3487971, 398.7738862, 399.9984842, 401.2225294, 402.4465745, 403.4956843, 404.4908077, 405.4859311, 406.4810545, 407.4761779, 408.4713012, 409.3282947, 410.1426603, 410.9570259, 411.7713915, 412.5857571, 413.4001227, 414.0982633, 414.7605361, 415.4228088, 416.0850816, 416.7473543, 417.4096271, 418.0319308, 418.6282585, 419.2091212, 419.7745189, 420.3244517, 420.8589196, 421.3714189, 421.8642265, 422.3390526, 422.7958975, 423.2347609, 423.655643,  424.0592165, 424.4452458, 424.813554,  425.1641411, 425.4970072, 425.8121522, 426.1144565, 426.4022116, 426.674134,  426.9302237, 427.1704806, 427.3949048, 427.6092447],
    [293.15,  295.7358955, 309.9466546, 335.6660931, 361.4825862, 382.990676,  399.8214205, 412.2296454, 421.1416965, 427.5569872, 432.3347821, 436.0954322, 439.2921995, 441.79704,   444.099442,  446.0724583, 448.0131845, 449.9539107, 451.6451833, 453.1490657, 454.6529481, 456.1568305, 457.6607128, 459.1645952, 460.4704859, 461.6276448, 462.7848036, 463.9419625, 465.0991214, 466.2562802, 467.2511161, 468.1240144, 468.9969128, 469.8698111, 470.7427095, 471.6156078, 472.4355721, 473.1936094, 473.9234325, 474.6250414, 475.2984361, 475.9436166, 476.5528248, 477.1247428, 477.6643115, 478.1715309, 478.646401,  479.0889218, 479.5031053, 479.8896331, 480.24595,   480.572056,  480.8679511, 481.1336354, 481.3779809, 481.6024949, 481.801527,  481.9750771, 482.1231452, 482.2457313, 482.3501653],
    [293.15,  296.8850201, 316.099278,  349.8316168, 383.2680091, 410.9086716, 432.5898918, 448.6863601, 460.4145209, 469.0396861, 475.6034276, 480.8636997, 485.4419228, 489.1315367, 492.1205118, 495.109487,  498.0984622, 500.6272167, 503.0730869, 505.518957,  507.7014609, 509.4612152, 511.2209695, 512.9807239, 514.7404782, 516.5002326, 518.0519192, 519.2696201, 520.4873211, 521.705022,  522.9227229, 524.1404239, 525.1936952, 525.9830279, 526.7723605, 527.5616931, 528.3510258, 529.1403584, 529.8792512, 530.5086941, 531.0969691, 531.6440762, 532.1500155, 532.614787,  533.0331077, 533.3987971, 533.7190069, 533.993737,  534.2229875, 534.4067584, 534.5514644, 534.6646105, 534.7375125, 534.7701706, 534.7625846, 534.7147547, 534.6361805, 534.5379759, 534.4072807, 534.244095,  534.0484188],
    [293.15,  298.3216914, 323.9543478, 367.284196,  408.8889908, 443.3974011, 470.2381359, 490.2998081, 505.1202238, 516.2546815, 524.9419532, 532.0469563, 538.2907413, 543.4791494, 547.4182305, 551.3573116, 555.2963926, 558.6587909, 561.6921056, 564.7254203, 567.7026393, 570.0051608, 572.3076823, 574.6102039, 576.7788069, 578.7258116, 580.5457009, 582.2384746, 583.8041328, 585.2426755, 586.5480241, 587.7178373, 588.7569255, 589.6652889, 590.4429273, 591.0898407, 591.6507722, 592.1429555, 592.530982,  592.8148517, 592.9945645, 593.0701204, 593.0871356, 593.0631802, 592.9621545, 592.7840585, 592.5288922, 592.1966557, 591.8247865, 591.4277048, 590.9757831, 590.4690214, 589.9074197, 589.2909779, 588.6482676, 587.9902936, 587.2944452, 586.5607223, 585.7891249, 584.979653,  584.1534559],
    [293.15,  300.2843191, 334.6900377, 390.4009905, 442.3138267, 485.2139716, 518.4973853, 543.519066,  562.2746266, 576.6655349, 588.1507893, 597.7239285, 606.1238714, 613.4332561, 619.9261352, 625.7158021, 631.0484705, 635.8139793, 640.0123286, 643.8652391, 647.2712805, 650.2162206, 652.797323,  655.2237274, 657.3429253, 659.1549165, 660.6597012, 661.8572793, 662.8252109, 663.6994941, 664.3427371, 664.7549399, 664.9361025, 664.8862248, 664.6862532, 664.4781232, 664.1184446, 663.6072175, 662.9444419, 662.1301177, 661.2222293, 660.3224495, 659.3280635, 658.2390714, 657.055473,  655.7772684, 654.4436729, 653.1234486, 651.7471285, 650.3147129, 648.8262016, 647.2815946, 645.7067323, 644.1469241, 642.5563963, 640.9351486, 639.2831812, 637.600494,  635.9038972, 634.2228663, 632.5276237],
    ],

    [   # extra_data = 1.1
    [293.15,  293.2015997, 293.9734368, 296.8312899, 302.1183162, 308.3944538, 314.9804723, 321.2167571, 326.7436774, 331.4450337, 335.3389253, 338.52271,   341.1153012, 343.2281263, 344.9343435, 346.2785026, 347.4076005, 348.2766658, 348.8444316, 348.9767656, 349.1090995, 349.2414335, 349.1476154, 349.0470854, 348.9465554, 348.6710991, 348.3593582, 348.0476172, 347.7358763, 347.4241353, 347.1123944, 346.7217065, 346.3146428, 345.9075792, 345.5005155, 345.0934518, 344.6863881, 344.2538938, 343.8161245, 343.3783552, 342.9405859, 342.5028166, 342.0650473, 341.6260177, 341.1863193, 340.7461753, 340.3055855, 339.86455,   339.4230689, 338.9875009, 338.554862,  338.1240263, 337.6949937, 337.2677644, 336.8423382, 336.4257976, 336.014819,  335.6081482, 335.2057855, 334.8077306, 334.4139838],
    [293.15,  293.5157904, 296.8560308, 305.3991692, 316.2378372, 326.8363206, 336.3724484, 344.3539151, 350.7258481, 355.6192097, 359.2581369, 361.888829,  363.7347,    365.0022037, 365.7732757, 366.112037,  366.2646007, 366.1697584, 365.8252068, 365.1215839, 364.3307721, 363.5399603, 362.7148077, 361.837488,  360.9601682, 360.0833845, 359.2113159, 358.3392473, 357.4671787, 356.5951101, 355.7230415, 354.8576514, 354.0509952, 353.2443389, 352.4376826, 351.6310264, 350.8243701, 350.0265599, 349.3065456, 348.5865313, 347.866517,  347.1465027, 346.4264884, 345.7096521, 345.0263869, 344.3533238, 343.6904629, 343.037804,  342.3953473, 341.763918,  341.1514076, 340.5517483, 339.9649402, 339.3909832, 338.8298774, 338.2818335, 337.7488674, 337.2294291, 336.7235186, 336.2311359, 335.7522811],
    [293.15,  294.0945155, 300.7650277, 315.5016566, 333.0037038, 349.3747871, 363.4639685, 374.7486358, 383.2849911, 389.4151711, 393.5906281, 396.2177942, 397.7379989, 398.3778274, 398.3768161, 397.8050341, 396.8440417, 395.7257564, 394.4197585, 392.9124632, 391.3410349, 389.6959627, 387.9428645, 386.2012783, 384.5312248, 382.8656915, 381.2046783, 379.5481853, 377.8962124, 376.2928294, 374.7462143, 373.2278036, 371.7375975, 370.2755959, 368.8417988, 367.4621448, 366.1414473, 364.8628944, 363.6264863, 362.4322228, 361.2801039, 360.1666629, 359.0912563, 358.0561312, 357.0612875, 356.1067253, 355.1924445, 354.3055488, 353.4436449, 352.6150916, 351.8198889, 351.0580366, 350.329535,  349.6213757, 348.931145,  348.2672739, 347.6297624, 347.0186105, 346.4338182, 345.8647846, 345.3095425],
    [293.15,  294.8474552, 305.2725548, 326.4699689, 350.3612962, 372.1208719, 390.2827331, 404.3061808, 414.3919132, 421.1259561, 425.2015482, 427.2339673, 427.8680024, 427.4317009, 426.2689382, 424.4488337, 422.250488,  419.9170259, 417.4650498, 414.8601232, 412.229455,  409.6041331, 406.9298712, 404.2764976, 401.7389712, 399.2454621, 396.8077457, 394.4848923, 392.2419342, 390.0788713, 387.9994344, 386.0018093, 384.0859119, 382.2517422, 380.4993002, 378.828586,  377.2005346, 375.6416805, 374.1530149, 372.7345376, 371.3862487, 370.1081481, 368.8517203, 367.6499194, 366.5039758, 365.4138896, 364.3796608, 363.4012895, 362.4350051, 361.5105385, 360.629, 359.7903897, 358.9947074, 358.2419532, 357.4970217, 356.7837581, 356.1030528, 355.4549059, 354.8393173, 354.256287,  353.6791268],
    [293.15,  295.7462283, 310.634747,  340.149575,  373.456559,  403.1514902, 427.5914917, 445.8604602, 458.4046004, 466.1201554, 470.0732085, 471.2898518, 470.5983605, 468.688874,  465.874701,  462.3110234, 458.4747079, 454.4037316, 450.3997047, 446.3515618, 442.2912667, 438.3861856, 434.5363926, 430.7418876, 427.1522564, 423.709372,  420.4009609, 417.2466088, 414.2518509, 411.4077567, 408.6997683, 406.0978791, 403.6228,    401.2745311, 399.0530724, 396.9584238, 394.9648171, 393.0312423, 391.2003594, 389.4721684, 387.8466692, 386.3238619, 384.8750438, 383.4545354, 382.1098543, 380.8410004, 379.6479736, 378.5307741, 377.4670954, 376.4214373, 375.4307283, 374.4949685, 373.6141578, 372.7882963, 372.001147,  371.2268689, 370.4923426, 369.7975682, 369.1425457, 368.527275,  367.9401927],
    [293.15,  296.8476101, 317.1860699, 356.3684295, 399.2831064, 436.6094283, 466.4494819, 487.8317224, 501.5796877, 509.0800793, 511.8798642, 511.3943998, 508.7289744, 504.7991061, 499.9552143, 494.3996734, 488.7194752, 482.853625,  477.0973576, 471.5122719, 466.1701349, 461.0313642, 456.1103332, 451.4313488, 446.9766355, 442.7463548, 438.7457582, 434.9719615, 431.4249645, 428.0676807, 424.8994228, 421.931892,  419.1297435, 416.4332102, 413.8860003, 411.4881135, 409.2395501, 407.1403099, 405.1521801, 403.2264913, 401.4178116, 399.726141,  398.1514795, 396.6938271, 395.3121479, 393.9541772, 392.6785143, 391.485159,  390.3741115, 389.3453718, 388.3692137, 387.4077771, 386.5035109, 385.656415,  384.8664895, 384.1337343, 383.4376521, 382.7521369, 382.1064588, 381.5006178, 380.9346139],
    [293.15,  298.2421895, 325.5681504, 376.3290388, 429.2541739, 474.432589,  508.9155975, 532.3793926, 546.1893046, 552.4142012, 553.2748119, 550.4276276, 545.3677481, 539.0731265, 532.0297455, 524.3873348, 516.8029738, 509.2273086, 501.9306228, 494.9740441, 488.3909531, 482.1544476, 476.2583888, 470.6953032, 465.4712215, 460.5822245, 455.9667774, 451.659518,  447.6604463, 443.8935255, 440.3606786, 437.0841935, 434.0124329, 431.0558979, 428.2799259, 425.684517,  423.2696711, 421.0353882, 418.9319698, 416.8939901, 414.993942,  413.2318257, 411.6076411, 410.1213881, 408.7211277, 407.3384846, 406.0492198, 404.8533335, 403.7508255, 402.741696,  401.7898882, 400.8479353, 399.9684315, 399.1513767, 398.3967711, 397.7046145, 397.0510171, 396.404529,  395.7999973, 395.2374221, 394.7168031],
    ],

    [   # extra_data = 1.2
    [293.15,  293.1748954, 293.5934969, 295.1369688, 298.4693039, 302.5862554, 307.0390589, 311.4003469, 315.3767741, 318.8234771, 321.7254569, 324.1238989, 326.0832269, 327.7002282, 329.0065319, 330.0527777, 330.909284,  331.6041742, 332.1209023, 332.3414345, 332.4275298, 332.5136251, 332.5418433, 332.4663094, 332.3907754, 332.2919576, 332.0722527, 331.8525478, 331.6328429, 331.4131379, 331.193433,  330.9632255, 330.6784899, 330.3937543, 330.1090187, 329.8242831, 329.5395474, 329.2514413, 328.9458358, 328.6402303, 328.3346249, 328.0290194, 327.7234139, 327.4176649, 327.1110032, 326.8040531, 326.4968144, 326.1892874, 325.8814718, 325.5741375, 325.2714093, 324.9699395, 324.6697283, 324.3707756, 324.0730813, 323.7774252, 323.4879846, 323.2013692, 322.9175792, 322.6366143, 322.3584747],
    [293.15,  293.3624068, 295.4988613, 301.220226,  309.6974112, 318.3763249, 326.4083409, 333.264157,  338.7787786, 343.0246419, 346.1717816, 348.4153323, 349.9478074, 350.9739068, 351.555171,  351.7705981, 351.8025871, 351.6350712, 351.256477,  350.5880252, 349.8619267, 349.1358282, 348.3801169, 347.5995101, 346.8189033, 346.0486312, 345.2970056, 344.5453801, 343.7937545, 343.042129,  342.2905034, 341.5646965, 340.8854737, 340.2062509, 339.5270281, 338.8478053, 338.1685825, 337.5193906, 336.9243829, 336.3293752, 335.7343676, 335.1393599, 334.5443522, 333.960108,  333.401726,  332.852841,  332.3134528, 331.7835615, 331.2631671, 330.754683,  330.261495,  329.7799333, 329.309998,  328.851689,  328.4050065, 327.9702316, 327.5477592, 327.1371613, 326.738438,  326.3515894, 325.9766153],
    [293.15,  293.7694621, 298.4663077, 309.0364421, 322.2970626, 334.9087608, 345.8456731, 354.5784058, 361.1089113, 365.6921114, 368.6734957, 370.4102861, 371.2327614, 371.420395,  371.0966305, 370.3526071, 369.4820099, 368.4016909, 367.1116501, 365.8097168, 364.4103316, 362.9037279, 361.4317349, 359.9789381, 358.5129689, 357.0893287, 355.7302475, 354.4077213, 353.1217501, 351.8723338, 350.6594724, 349.4875663, 348.3570314, 347.2653034, 346.2123823, 345.198268,  344.2229606, 343.2830554, 342.3782305, 341.51047,   340.679774,  339.8861424, 339.1295752, 338.3974645, 337.6886179, 337.0103833, 336.3627607, 335.7457501, 335.1593516, 334.5902601, 334.0372175, 333.5079779, 333.0025413, 332.5209075, 332.0630767, 331.6181097, 331.1849719, 330.7700386, 330.3733099, 329.9947858, 329.6344662],
    [293.15,  294.3394772, 302.0568223, 317.9279833, 336.5646272, 353.6689985, 367.9208463, 378.7629068, 386.3699328, 391.2156634, 393.8738982, 394.9063018, 394.8027997, 393.9664766, 392.56351,   390.7139046, 388.8019236, 386.7183574, 384.463206,  382.2531265, 380.007794,  377.7086735, 375.4922147, 373.3648271, 371.2834029, 369.2804757, 367.3815512, 365.5633786, 363.8241801, 362.1596025, 360.5724912, 359.062846,  357.630667,  356.2759542, 354.9853139, 353.7331513, 352.5447016, 351.4199648, 350.3589411, 349.3616304, 348.412799,  347.4833355, 346.6019424, 345.7686196, 344.9833671, 344.2461849, 343.5446141, 342.8548456, 342.200354,  341.5811393, 340.9972013, 340.4485403, 339.9258486, 339.4113398, 338.9225506, 338.4594808, 338.0221305, 337.6104998, 337.2178765, 336.8314341, 336.463819],
    [293.15,  295.0380798, 306.1819062, 327.5182507, 350.7736541, 371.4573582, 387.9305066, 399.8155517, 407.5179648, 411.7922012, 413.5302426, 413.4257193, 412.1549685, 410.0885684, 407.5459991, 404.6572701, 401.7538229, 398.7186273, 395.6314844, 392.6530648, 389.67541,   386.7337382, 383.9946906, 381.3606825, 378.8341223, 376.4648817, 374.2263528, 372.1185355, 370.1009171, 368.1893722, 366.386727,  364.6929816, 363.1081359, 361.6321899, 360.191092,  358.829631,  357.5536704, 356.3632102, 355.2582504, 354.238791,  353.2252862, 352.265848,  351.3667747, 350.5280664, 349.7497232, 349.0317449, 348.3154957, 347.6364403, 346.9992218, 346.40384,   345.850295,  345.3385869, 344.8281976, 344.3436338, 343.8881036, 343.461607,  343.0641442, 342.695715,  342.3287827, 341.9800023, 341.6515543],
    [293.15,  295.8714916, 311.2228799, 341.4849667, 375.0537906, 404.692879,  427.6837127, 443.5680642, 453.1323722, 457.7659355, 458.8012303, 457.5626391, 454.7561833, 450.9220739, 446.4595538, 441.6406525, 436.7763291, 432.0376411, 427.4624628, 423.0208882, 418.8024674, 414.7768913, 410.9367576, 407.3378158, 403.9559899, 400.7890944, 397.8079385, 395.0270204, 392.4404961, 389.9539328, 387.615727,  385.4258786, 383.3843876, 381.491254,  379.7272363, 378.0106313, 376.4093028, 374.9232508, 373.5524753, 372.2969763, 371.121904,  369.9600377, 368.876935,  367.8725958, 366.9470201, 366.1002079, 365.2974844, 364.5082079, 363.7718353, 363.0883667, 362.4578021, 361.8801414, 361.3249625, 360.7835008, 360.2774688, 359.8068665, 359.3716939, 358.9719511, 358.5875528, 358.2128711, 357.8622884],
    [293.15,  296.8853532, 317.3764519, 357.1712897, 401.6161566, 439.9961037, 468.8724863, 488.0384876, 498.8703133, 503.2330317, 503.0305916, 499.9728358, 495.2734753, 489.5191844, 483.0166472, 476.3561061, 469.7364158, 463.291609,  457.2138173, 451.4354215, 445.9661769, 440.8270787, 436.004726,  431.4936183, 427.2822785, 423.3780797, 419.7552494, 416.3616557, 413.2310107, 410.3156491, 407.522092,  404.9111981, 402.4829672, 400.2373994, 398.1744948, 396.2431483, 394.3758926, 392.6473449, 391.0575053, 389.6063738, 388.2939503, 387.0629108, 385.8430977, 384.7142591, 383.6763951, 382.7295057, 381.8735907, 381.0685747, 380.2690445, 379.5281517, 378.8458963, 378.2222783, 377.6572978, 377.124467,  376.5960367, 376.1055151, 375.6529023, 375.2381982, 374.8614028, 374.5057083, 374.1535223],
    ],

    [   # extra_data = 1.3
    [293.15,  293.1629088, 293.403606,  294.4482898, 296.6011282, 299.3046792, 302.279801,  305.2461985, 307.9960897, 310.4167833, 312.4776441, 314.1994445, 315.6280732, 316.811888,  317.6144353, 318.325076,  318.8621994, 319.2622674, 319.5352004, 319.8081333, 320.0202608, 320.0426034, 320.0649459, 320.0872885, 320.109631,  320.1319736, 320.1230199, 320.0163851, 319.9097503, 319.8031154, 319.6964806, 319.5898458, 319.4683293, 319.3003645, 319.1323997, 318.964435,  318.7964702, 318.6285054, 318.4577287, 318.2758688, 318.0902962, 317.901011,  317.7080131, 317.5113026, 317.3120594, 317.1137548, 316.9132954, 316.7106815, 316.505913,  316.2989898, 316.091541,  315.8883585, 315.6851722, 315.4819822, 315.2787884, 315.0755908, 314.8737529, 314.6772852, 314.4826138, 314.2897388, 314.0986601],
    [293.15,  293.2827681, 294.7461118, 298.7937922, 305.3973485, 312.39599,   319.0209985, 324.7965996, 329.5328224, 333.2303696, 336.0142112, 338.0322569, 339.4317441, 340.3765258, 340.9425158, 341.222296,  341.2704796, 341.1911369, 340.944491,  340.4947271, 339.8997826, 339.3048382, 338.7073014, 338.0707662, 337.434231,  336.7976958, 336.1822232, 335.5710374, 334.9598515, 334.3486656, 333.7374798, 333.1262939, 332.5641941, 332.0120845, 331.4599749, 330.9078652, 330.3557556, 329.8036459, 329.308139,  328.824152,  328.340165,  327.856178,  327.372191,  326.888204,  326.4259804, 325.9752066, 325.5321017, 325.0966657, 324.6688986, 324.2488004, 323.8412428, 323.4439171, 323.055977,  322.6774225, 322.3082535, 321.9484701, 321.5985994, 321.2583915, 320.927755,  320.6066898, 320.2951959],
    [293.15,  293.5752061, 297.0589211, 305.2055494, 316.5082797, 327.5463894, 337.299161,  345.2355009, 351.2654672, 355.547744,  358.3868264, 360.0772466, 360.9309195, 361.1643333, 360.9444828, 360.3088186, 359.448078,  358.3949326, 357.215983,  356.0309618, 354.803629,  353.5339846, 352.2744457, 351.0210715, 349.7604533, 348.5262465, 347.3483688, 346.2004353, 345.0824459, 343.9944006, 342.9362994, 341.9136454, 340.9294264, 339.9786648, 339.0613605, 338.1775137, 337.3271241, 336.5083927, 335.7203423, 334.9646005, 334.2411674, 333.550043,  332.8912271, 332.2560428, 331.6397786, 331.0502833, 330.487557,  329.9515997, 329.4424113, 328.9506318, 328.4711789, 328.0125192, 327.5746527, 327.1575796, 326.7612997, 326.3780797, 326.0037208, 325.6452182, 325.3025716, 324.9757813, 324.6648471],
    [293.15,  294.0183425, 299.9640929, 312.6269921, 328.3209746, 342.9175762, 355.2131181, 364.6659729, 371.3349427, 375.6188812, 377.9902712, 378.9183876, 378.8059547, 378.0887197, 376.8571666, 375.2813553, 373.5643939, 371.7705008, 369.8558898, 367.9152851, 366.0042124, 364.0645094, 362.1387163, 360.3273394, 358.5637197, 356.8512462, 355.2369905, 353.6949818, 352.2252202, 350.8171893, 349.4739955, 348.1970094, 346.9862308, 345.8416598, 344.7632964, 343.7150639, 342.7153757, 341.7695491, 340.8775841, 340.0394806, 339.2552388, 338.4846279, 337.7481814, 337.0518289, 336.3955704, 335.7794059, 335.2033354, 334.6353875, 334.0918801, 333.5775256, 333.092324,  332.6362752, 332.2093793, 331.7881566, 331.3845911, 331.0021433, 330.6408133, 330.3006011, 329.9815066, 329.6667646, 329.3649318],
    [293.15,  294.5730902, 303.389663,  321.2187874, 342.5218512, 361.803484,  377.4485941, 388.8971626, 396.4488886, 400.7517954, 402.5592293, 402.5843717, 401.43197,   399.5879569, 397.2293961, 394.4907621, 391.7870652, 389.0022787, 386.1364024, 383.3680701, 380.6546971, 377.9674292, 375.3989524, 372.9833804, 370.6748708, 368.483599,  366.4267715, 364.49211,   362.6734766, 360.9282503, 359.2809225, 357.7314933, 356.2799625, 354.9263303, 353.660507,  352.422783,  351.2610696, 350.1753668, 349.1656747, 348.2319932, 347.3637083, 346.4980068, 345.6852905, 344.9255592, 344.2188131, 343.565052,  342.9566324, 342.348321,  341.7764133, 341.2409094, 340.7418092, 340.2791127, 339.8476147, 339.4165116, 339.0105203, 338.629641,  338.2738735, 337.943218,  337.6341659, 337.3259546, 337.0352442],
    [293.15,  295.2401695, 307.2940799, 330.2543727, 355.388369,  377.3511093, 394.2662368, 405.9064732, 412.8908424, 416.2043436, 416.8200644, 415.6121757, 413.4288502, 410.4889466, 407.0433334, 403.466819,  399.7712227, 396.1406137, 392.667686,  389.3508836, 386.1792422, 383.1755911, 380.335879,  377.6559384, 375.1167271, 372.7175863, 370.4641686, 368.356474,  366.3945025, 364.5782541, 362.8362374, 361.1855606, 359.6507285, 358.2317409, 356.9285979, 355.7412996, 354.5852289, 353.4806352, 352.456522,  351.5128894, 350.6497374, 349.8670659, 349.0995046, 348.3626972, 347.6790501, 347.0485633, 346.4712367, 345.9470705, 345.4318149, 344.9360593, 344.4749707, 344.0485491, 343.6567945, 343.299707,  342.9489286, 342.6112455, 342.2963778, 342.0043254, 341.7350884, 341.4886668, 341.247025],
    [293.15,  296.0313509, 311.9686135, 341.2648903, 372.2116803, 398.4700698, 418.0092621, 430.7893735, 437.8402195, 440.4805341, 440.0094991, 437.6120682, 434.1635874, 429.9960827, 425.348628,  420.6586049, 415.9652918, 411.4212986, 407.1459193, 403.0982116, 399.2781819, 395.6901805, 392.3319899, 389.20361,   386.2311692, 383.4442873, 380.8473656, 378.4404041, 376.2234027, 374.1963615, 372.2185577, 370.3772895, 368.6821206, 367.1330507, 365.73008,   364.4732084, 363.204277,  362.0214008, 360.9353281, 359.946059,  359.0535934, 358.2579313, 357.4451607, 356.6859478, 355.9880338, 355.3514189, 354.7761029, 354.2620859, 353.7361811, 353.2437905, 352.7898877, 352.3744727, 351.9975457, 351.6591064, 351.3141357, 350.9905615, 350.6914434, 350.4167812, 350.1665752, 349.9408252, 349.7118711],
    ],

    [   # extra_data = 1.4
    [293.15,  293.1567008, 293.3103477, 293.9929461, 295.5264314, 297.5905597, 299.976411,  302.4230958, 304.7197588, 306.7686681, 308.532167,  310.0175541, 311.2577626, 312.2993934, 313.0569785, 313.7002866, 314.1891932, 314.5980943, 314.8610379, 315.1239815, 315.3667141, 315.4165006, 315.4662872, 315.5160737, 315.5658602, 315.6156468, 315.6546495, 315.5907034, 315.5267574, 315.4628113, 315.3988652, 315.3349192, 315.2655517, 315.1444287, 315.0233056, 314.9021826, 314.7810595, 314.6599364, 314.5377396, 314.4032573, 314.2650587, 314.1231439, 313.9775129, 313.8281655, 313.675455,  313.5230672, 313.368185,  313.2108083, 313.0509371, 312.8885714, 312.7242463, 312.5635483, 312.4022075, 312.240224,  312.0775977, 311.9143286, 311.7508494, 311.5916767, 311.4333583, 311.2758942, 311.1192845],
    [293.15,  293.2348812, 294.2600281, 297.3526214, 302.2403836, 307.5588291, 312.707056,  317.2320655, 320.9700401, 323.9111158, 326.1414674, 327.7817181, 328.9566464, 329.7678054, 330.2895575, 330.5573183, 330.7046926, 330.6894743, 330.4987394, 330.0974537, 329.696168,  329.2948822, 328.842146,  328.3831553, 327.9241646, 327.4627033, 327.0001661, 326.5376289, 326.0750917, 325.6125545, 325.1500173, 324.7111039, 324.2824789, 323.8538539, 323.4252289, 322.9966039, 322.5679789, 322.17205,   321.7903607, 321.4086714, 321.026982,  320.6452927, 320.2636034, 319.8948791, 319.5365166, 319.1837125, 318.8364669, 318.4947798, 318.1586512, 317.8314437, 317.5124822, 317.2005208, 316.8955595, 316.5975984, 316.3066375, 316.0234086, 315.7477648, 315.479435,  315.2184191, 314.9647171, 314.7183291],
    [293.15,  293.4524173, 296.0630065, 302.5157022, 310.8837293, 319.2012351, 326.552156,  332.529899,  337.048958,  340.2619042, 342.3867875, 343.6531144, 344.330737,  344.5222707, 344.3539174, 343.9105603, 343.264382,  342.5645976, 341.7652075, 340.8661921, 339.9138368, 338.9614816, 338.0091263, 337.1122786, 336.224494,  335.3367095, 334.5517738, 333.8079959, 333.0642179, 332.32044,   331.576662,  330.8328841, 330.1836797, 329.5723215, 328.9609633, 328.3496052, 327.738247,  327.1268888, 326.5962654, 326.0979502, 325.5996351, 325.1013199, 324.6030048, 324.1046896, 323.6333366, 323.1824116, 322.742732,  322.3142977, 321.8971088, 321.4911652, 321.0997645, 320.7221073, 320.3570709, 320.004655,  319.6648598, 319.3376853, 319.0211286, 318.7156751, 318.422007,  318.1401242, 317.8700267],
    [293.15,  293.8013681, 298.5092185, 308.8293627, 322.3142872, 335.0591716, 345.9340935, 354.4123485, 360.4888157, 364.4446593, 366.718804,  367.6986593, 367.7356115, 367.1746988, 366.1675418, 364.8825718, 363.3853077, 361.8592887, 360.2369772, 358.5462675, 356.9088371, 355.2508297, 353.5722451, 351.9979736, 350.4708596, 348.9857064, 347.5674929, 346.2183207, 344.9295937, 343.701312,  342.5334755, 341.4260843, 340.3596077, 339.3373855, 338.3670719, 337.448667,  336.5821707, 335.7675832, 334.9791713, 334.2213353, 333.5041604, 332.8276466, 332.1917939, 331.5966023, 331.017625,  330.4590423, 329.9304353, 329.4318039, 328.9631482, 328.5244683, 328.0967171, 327.6831515, 327.2912364, 326.9209718, 326.5723577, 326.2453941, 325.926388,  325.6176808, 325.324639,  325.0472626, 324.7855517],
    [293.15,  294.253775,  301.3589427, 316.0308703, 334.0937277, 350.5999794, 364.1239343, 374.1232813, 380.7991666, 384.6839492, 386.4055815, 386.555881,  385.6548966, 384.1608445, 382.1964629, 379.9148039, 377.6100729, 375.2600024, 372.8426685, 370.4762128, 368.1743719, 365.8948527, 363.6928557, 361.6312527, 359.6596709, 357.7827452, 356.0207235, 354.3614023, 352.8047817, 351.3090887, 349.8952544, 348.5638999, 347.3150254, 346.1486308, 345.0647161, 344.0005497, 342.9994918, 342.0625908, 341.1898467, 340.3812595, 339.6368292, 338.8904826, 338.1878898, 337.5301548, 336.9172776, 336.3492584, 335.826097,  335.3000719, 334.8041685, 334.3391842, 333.9051189, 333.5019728, 333.1297458, 332.7558361, 332.4027783, 332.071117,  331.7608523, 331.4719842, 331.2045127, 330.9363939, 330.6828646],
    [293.15,  294.8003593, 304.6089055, 323.8273753, 345.3735592, 364.386704,  379.3616191, 389.8598753, 396.3387573, 399.5660133, 400.3773869, 399.5478348, 397.6778042, 395.2302812, 392.4009333, 389.3068294, 386.308487,  383.2973753, 380.2734941, 377.4201852, 374.6453747, 371.9470253, 369.4221597, 367.0524589, 364.8199474, 362.7260551, 360.7712215, 358.9547948, 357.2488701, 355.6194678, 354.0929249, 352.6692415, 351.3484174, 350.1304528, 348.9803011, 347.8692965, 346.8360473, 345.8805533, 345.0028146, 344.2028311, 343.4444893, 342.6982505, 342.0038984, 341.361433,  340.7708543, 340.2321624, 339.7206808, 339.2162261, 338.7459821, 338.309949,  337.9081268, 337.5405154, 337.1910761, 336.8466905, 336.525027,  336.2260857, 335.9498666, 335.6963697, 335.4552068, 335.217881,  334.9958362],
    [293.15,  295.4403458, 308.3987413, 332.8022515, 359.1600534, 381.8271988, 398.8822493, 410.2206962, 416.6146872, 419.2102873, 419.0776784, 417.1471811, 414.3289216, 410.833571,  406.9330735, 402.9610636, 398.9518028, 395.0787957, 391.3998242, 387.9266597, 384.646569,  381.5606437, 378.6688265, 375.9708437, 373.4250445, 371.0224925, 368.7795958, 366.6963543, 364.7727679, 363.0088368, 361.3250146, 359.7277538, 358.2533716, 356.901868,  355.673243,  354.5674966, 353.4954037, 352.4642019, 351.5146272, 350.6466797, 349.8603595, 349.1556664, 348.468296,  347.8034645, 347.1905303, 346.6294935, 346.120354,  345.6631119, 345.2163319, 344.7833751, 344.3831589, 344.0156834, 343.6809485, 343.3789543, 343.0841014, 342.7984662, 342.5337364, 342.2899119, 342.0669927, 341.8649788, 341.6680651],
    ],

    [   # extra_data = 1.5
    [293.15,  293.1535548, 293.2534792, 293.7124124, 294.7498914, 296.1178109, 297.6843003, 299.2949272, 300.8250434, 302.20022,   303.3923962, 304.4049431, 305.2578463, 305.9792114, 306.5031476, 306.9589424, 307.3108352, 307.6203763, 307.8136766, 308.0069768, 308.2002771, 308.2747408, 308.3246526, 308.3745643, 308.4244761, 308.4743879, 308.5242997, 308.5088067, 308.4798009, 308.450795,  308.4217892, 308.3927834, 308.3637776, 308.3003439, 308.2297972, 308.1592506, 308.0887039, 308.0181573, 307.9476106, 307.8690141, 307.7861533, 307.7004478, 307.6118975, 307.5205025, 307.4262628, 307.331324,  307.234677,  307.1359436, 307.0351237, 306.9322172, 306.8272243, 306.723715,  306.6200104, 306.515481,  306.4101267, 306.3039475, 306.1969435, 306.0921601, 305.988165,  305.8844213, 305.780929],
    [293.15,  293.2064,    293.9528551, 296.3201197, 300.2376569, 304.6075469, 308.9343959, 312.8014232, 316.041521,  318.6286716, 320.6191444, 322.1086476, 323.1969548, 323.9778937, 324.5018581, 324.8012244, 324.9966829, 325.0529642, 324.9700683, 324.6761384, 324.3733292, 324.0705201, 323.7254592, 323.364983,  323.0045069, 322.6364766, 322.2616429, 321.8868093, 321.5119756, 321.137142,  320.7623083, 320.3984818, 320.0445682, 319.6906547, 319.3367412, 318.9828277, 318.6289142, 318.2931711, 317.9737924, 317.6544138, 317.3350351, 317.0156564, 316.6962777, 316.384224,  316.0820228, 315.7840881, 315.4904199, 315.2010182, 314.915883,  314.6371402, 314.3655234, 314.0994113, 313.838804,  313.5837015, 313.3341036, 313.090646,  312.8535476, 312.6223241, 312.3969755, 312.1775016, 311.9639026],
    [293.15,  293.3674284, 295.4078936, 300.642957,  307.9574564, 315.356866,  322.0794326, 327.6370978, 331.9302514, 335.044374,  337.1579376, 338.4816231, 339.2105496, 339.5192222, 339.4891395, 339.1745145, 338.7714389, 338.2234357, 337.530505,  336.7028892, 335.8682393, 335.0335894, 334.2238838, 333.4269163, 332.6299489, 331.883359,  331.2010281, 330.5186973, 329.8363665, 329.1540356, 328.4717048, 327.8392938, 327.2705583, 326.7018227, 326.1330872, 325.5643516, 324.9956161, 324.4710533, 324.0028354, 323.5346174, 323.0663995, 322.5981815, 322.1299636, 321.6761207, 321.2479261, 320.8298912, 320.422016,  320.0243003, 319.6367443, 319.2612851, 318.8994419, 318.5491275, 318.2103417, 317.8830848, 317.5673565, 317.2622483, 316.9670473, 316.6827328, 316.4093048, 316.1467633, 315.8951082],
    [293.15,  293.6455098, 297.4072247, 305.9580909, 316.6930378, 326.9852718, 335.7852976, 342.6507558, 347.5736223, 350.7882903, 352.6471327, 353.4755573, 353.5894187, 353.196635,  352.4622212, 351.4184267, 350.2262205, 348.9681649, 347.689362,  346.3635471, 345.0370514, 343.7366143, 342.4342533, 341.156561,  339.9556397, 338.7957962, 337.6770307, 336.5993431, 335.5627334, 334.5675957, 333.6145126, 332.7028636, 331.8326488, 331.003868,  330.2165213, 329.4651646, 328.7417497, 328.0548486, 327.4044612, 326.7905876, 326.2132276, 325.6630159, 325.1261071, 324.6172476, 324.1364373, 323.6836761, 323.2589642, 322.8538553, 322.4558633, 322.0782869, 321.7211261, 321.3843808, 321.0680511, 320.7658538, 320.4684999, 320.1858828, 319.9180024, 319.6648588, 319.426452,  319.1983685, 318.974084],
    [293.15,  294.021614,  299.8640662, 312.2081027, 327.8738555, 342.4048859, 354.4387435, 363.4679385, 369.5843408, 373.2525868, 374.9961825, 375.3252842, 374.6687936, 373.4641811, 371.8259991, 369.9307583, 367.9185515, 365.9052409, 363.8351695, 361.7652876, 359.7731594, 357.7996464, 355.8599182, 354.0542009, 352.3242707, 350.6701276, 349.1123193, 347.643047,  346.2605606, 344.9441268, 343.6893639, 342.5048408, 341.3905573, 340.3465136, 339.3727097, 338.4364206, 337.5395898, 336.6976692, 335.9106587, 335.1785584, 334.5013683, 333.8445035, 333.2100178, 332.6142414, 332.0571742, 331.5388164, 331.0591679, 330.5930223, 330.1418766, 329.7176327, 329.3202904, 328.9498499, 328.606311,  328.272299,  327.9488455, 327.6441547, 327.3582265, 327.091061,  326.8426581, 326.6011728, 326.3673085],
    [293.15,  294.478028,  302.6378629, 319.0587701, 338.4365186, 355.7706393, 369.5721627, 379.3901576, 385.5770215, 388.793751,  389.7817157, 389.2445945, 387.7232736, 385.6425259, 383.1889584, 380.4558376, 377.6882867, 374.9248911, 372.2765718, 369.6986513, 367.2143502, 364.8594796, 362.6080705, 360.463636,  358.4428885, 356.5359408, 354.7427929, 353.0634449, 351.4978967, 350.0329282, 348.6162268, 347.2920428, 346.0603761, 344.9212268, 343.8745949, 342.9039493, 341.943876,  341.0497075, 340.2214438, 339.4590849, 338.7626308, 338.1184818, 337.4728224, 336.8711741, 336.3135368, 335.7999105, 335.3302954, 334.895282,  334.4576378, 334.0488571, 333.66894,   333.3178865, 332.9956965, 332.6963101, 332.395747,  332.1142917, 331.851944,  331.6087041, 331.3845719, 331.1756866, 330.9667711],
    [293.15,  295.0090535, 305.8510007, 327.0653214, 351.4431744, 372.768126,  389.2829089, 400.59167,   407.2907653, 410.3178352, 410.6679301, 409.2311139, 406.7092223, 403.6365891, 400.1986101, 396.528983,  393.0163113, 389.5491128, 386.1273876, 382.889134,  379.7954574, 376.8274288, 374.0416668, 371.4540325, 369.0392498, 366.7890924, 364.6915888, 362.7556237, 360.9667444, 359.2450867, 357.6374726, 356.1439021, 354.7643751, 353.4988917, 352.3311363, 351.1851587, 350.1237104, 349.1467913, 348.2544014, 347.4465407, 346.7067591, 345.9584802, 345.2649728, 344.6262369, 344.0422725, 343.5130795, 343.0277992, 342.5358825, 342.079094,  341.6574336, 341.2709012, 340.919497,  340.596373,  340.2696519, 339.9656713, 339.6844313, 339.4259318, 339.1901728, 338.972831,  338.7537809, 338.5496505],
    ]
    ])

# print("time",time_data.shape)
# print("ratio",ratio_data.shape)
# print("extra", extra_data.shape)
# print(p_data.shape)

# quit()


class MetaTempGroup(om.Group):
    def initialize(self):
        self.options.declare('num_nodes', types=int)

    def setup(self):
        nn = self.options['num_nodes']

        # self.add_input('ratio', 1, desc='')
        # self.add_input('time', 1, units='s', desc='time stamp of temperature data')
        # self.add_input('extra', 1, desc='additional case material')

        temp_interp = om.MetaModelStructuredComp(method='scipy_cubic')

        time_data = np.linspace(0,60,61)  # start, stop, # of elements
        ratio_data = np.linspace(0.5,2.0,7)
        extra_data = np.linspace(1.,1.5,6) 

        temp_interp.add_input('extra', val=1, training_data=extra_data, units='mm')
        temp_interp.add_input('ratio', val=1, training_data=ratio_data)
        temp_interp.add_input('time', val=1, training_data= time_data, units='s')
        temp_interp.add_output('temp_data', 300, training_data=t_data, units='K')

        self.add_subsystem('meta_temp_data', temp_interp,
            promotes=['*'])





# temp_interp = om.MetaModelStructuredComp(method='scipy_cubic')

# temp_interp.add_input('extra_data', val=1, training_data=extra_data, units='mm')
# temp_interp.add_input('ratio_data', val=1, training_data=ratio_data)
# temp_interp.add_input('time_data', val=1, training_data= time_data, units='s')

# temp_interp.add_output('t_data', 300, training_data=p_data)


# model = om.Group()
# model.add_subsystem('temp', temp_interp, promotes=['*'])
# prob = om.Problem(model)
# prob.setup()

# prob.set_val('ratio_data', 2.)        
# prob.set_val('time_data', 60)        
# prob.set_val('extra_data', 1)    

# prob.run_model()

# computed = prob.get_val('t_data')
# actual = 293.15                      

# print(computed)