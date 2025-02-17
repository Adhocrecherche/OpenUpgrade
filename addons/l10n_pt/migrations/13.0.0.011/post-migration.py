# Copyright 2022 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(
        env,
        [
            "l10n_pt.tag_compiva0",
            "l10n_pt.tag_compiva13",
            "l10n_pt.tag_compiva23",
            "l10n_pt.tag_compiva6",
            "l10n_pt.tag_iva0",
            "l10n_pt.tag_iva13",
            "l10n_pt.tag_iva23",
            "l10n_pt.tag_iva6",
        ],
    )
    openupgrade.load_data(
        env.cr, "l10n_pt", "migrations/13.0.0.011/noupdate_changes.xml",
    )
    openupgrade.set_xml_ids_noupdate_value(
        env,
        "l10n_pt",
        [
            "chart_13",
            "chart_1411",
            "chart_1412",
            "chart_1421",
            "chart_1422",
            "chart_1431",
            "chart_1432",
            "chart_2111",
            "chart_2112",
            "chart_2113",
            "chart_2114",
            "chart_2115",
            "chart_2116",
            "chart_2121",
            "chart_2122",
            "chart_2123",
            "chart_2124",
            "chart_2125",
            "chart_2126",
            "chart_218",
            "chart_219",
            "chart_2211",
            "chart_2212",
            "chart_2213",
            "chart_2214",
            "chart_2215",
            "chart_2216",
            "chart_2221",
            "chart_2222",
            "chart_2223",
            "chart_2224",
            "chart_2225",
            "chart_2226",
            "chart_225",
            "chart_229",
            "chart_2311",
            "chart_2312",
            "chart_2321",
            "chart_2322",
            "chart_2371",
            "chart_2372",
            "chart_2381",
            "chart_239",
            "chart_2431",
            "chart_2432",
            "chart_2433",
            "chart_2434",
            "chart_2435",
            "chart_2436",
            "chart_2437",
            "chart_2438",
            "chart_2439",
            "chart_244",
            "chart_245",
            "chart_246",
            "chart_248",
            "chart_2511",
            "chart_2512",
            "chart_2513",
            "chart_2521",
            "chart_2531",
            "chart_2532",
            "chart_254",
            "chart_258",
            "chart_261",
            "chart_262",
            "chart_263",
            "chart_264",
            "chart_265",
            "chart_266",
            "chart_268",
            "chart_269",
            "chart_2711",
            "chart_2712",
            "chart_2713",
            "chart_2721",
            "chart_2722",
            "chart_273",
            "chart_2741",
            "chart_2742",
            "chart_275",
            "chart_276",
            "chart_278",
            "chart_279",
            "chart_281",
            "chart_282",
            "chart_291",
            "chart_292",
            "chart_293",
            "chart_294",
            "chart_295",
            "chart_296",
            "chart_297",
            "chart_298",
            "chart_311",
            "chart_312",
            "chart_313",
            "chart_317",
            "chart_318",
            "chart_325",
            "chart_326",
            "chart_329",
            "chart_331",
            "chart_332",
            "chart_333",
            "chart_334",
            "chart_335",
            "chart_339",
            "chart_346",
            "chart_349",
            "chart_351",
            "chart_352",
            "chart_359",
            "chart_36",
            "chart_3711",
            "chart_3712",
            "chart_3721",
            "chart_3722",
            "chart_382",
            "chart_383",
            "chart_384",
            "chart_385",
            "chart_386",
            "chart_387",
            "chart_39",
            "chart_4111",
            "chart_4112",
            "chart_4113",
            "chart_4121",
            "chart_4122",
            "chart_4123",
            "chart_4131",
            "chart_4132",
            "chart_4133",
            "chart_4141",
            "chart_4142",
            "chart_4151",
            "chart_4158",
            "chart_419",
            "chart_421",
            "chart_422",
            "chart_426",
            "chart_428",
            "chart_429",
            "chart_431",
            "chart_432",
            "chart_433",
            "chart_434",
            "chart_435",
            "chart_436",
            "chart_437",
            "chart_438",
            "chart_439",
            "chart_441",
            "chart_442",
            "chart_443",
            "chart_444",
            "chart_446",
            "chart_448",
            "chart_449",
            "chart_451",
            "chart_452",
            "chart_453",
            "chart_454",
            "chart_455",
            "chart_459",
            "chart_469",
            "chart_51",
            "chart_521",
            "chart_522",
            "chart_53",
            "chart_54",
            "chart_551",
            "chart_552",
            "chart_56",
            "chart_5711",
            "chart_5712",
            "chart_5713",
            "chart_579",
            "chart_5811",
            "chart_5812",
            "chart_5891",
            "chart_5892",
            "chart_591",
            "chart_592",
            "chart_593",
            "chart_594",
            "chart_599",
            "chart_611",
            "chart_612",
            "chart_613",
            "chart_621",
            "chart_6221",
            "chart_6222",
            "chart_6223",
            "chart_6224",
            "chart_6225",
            "chart_6226",
            "chart_6228",
            "chart_6231",
            "chart_6232",
            "chart_6233",
            "chart_6234",
            "chart_6238",
            "chart_6241",
            "chart_6242",
            "chart_6243",
            "chart_6248",
            "chart_6251",
            "chart_6252",
            "chart_6253",
            "chart_6258",
            "chart_6261",
            "chart_6262",
            "chart_6263",
            "chart_6264",
            "chart_6265",
            "chart_6266",
            "chart_6267",
            "chart_6268",
            "chart_631",
            "chart_632",
            "chart_6331",
            "chart_6332",
            "chart_634",
            "chart_635",
            "chart_636",
            "chart_637",
            "chart_638",
            "chart_641",
            "chart_642",
            "chart_643",
            "chart_6511",
            "chart_6512",
            "chart_652",
            "chart_653",
            "chart_654",
            "chart_655",
            "chart_656",
            "chart_657",
            "chart_658",
            "chart_661",
            "chart_662",
            "chart_663",
            "chart_664",
            "chart_671",
            "chart_672",
            "chart_673",
            "chart_674",
            "chart_675",
            "chart_676",
            "chart_677",
            "chart_678",
            "chart_6811",
            "chart_6812",
            "chart_6813",
            "chart_682",
            "chart_683",
            "chart_6841",
            "chart_6842",
            "chart_6848",
            "chart_6851",
            "chart_6852",
            "chart_6853",
            "chart_6858",
            "chart_6861",
            "chart_6862",
            "chart_6868",
            "chart_6871",
            "chart_6872",
            "chart_6873",
            "chart_6874",
            "chart_6878",
            "chart_6881",
            "chart_6882",
            "chart_6883",
            "chart_6884",
            "chart_6885",
            "chart_6886",
            "chart_6888",
            "chart_6911",
            "chart_6918",
            "chart_692",
            "chart_6921",
            "chart_6928",
            "chart_6981",
            "chart_6988",
            "chart_711",
            "chart_712",
            "chart_713",
            "chart_714",
            "chart_716",
            "chart_717",
            "chart_718",
            "chart_721",
            "chart_722",
            "chart_725",
            "chart_726",
            "chart_728",
            "chart_731",
            "chart_732",
            "chart_733",
            "chart_734",
            "chart_741",
            "chart_742",
            "chart_743",
            "chart_744",
            "chart_751",
            "chart_752",
            "chart_7611",
            "chart_7612",
            "chart_7613",
            "chart_76211",
            "chart_76212",
            "chart_7622",
            "chart_7623",
            "chart_7624",
            "chart_7625",
            "chart_7626",
            "chart_7627",
            "chart_7628",
            "chart_7631",
            "chart_7632",
            "chart_7633",
            "chart_7634",
            "chart_7635",
            "chart_7636",
            "chart_7637",
            "chart_7638",
            "chart_771",
            "chart_772",
            "chart_773",
            "chart_774",
            "chart_7811",
            "chart_7812",
            "chart_7813",
            "chart_7814",
            "chart_7815",
            "chart_7816",
            "chart_783",
            "chart_7841",
            "chart_7842",
            "chart_7848",
            "chart_7851",
            "chart_7852",
            "chart_7858",
            "chart_7861",
            "chart_7862",
            "chart_7868",
            "chart_7871",
            "chart_7872",
            "chart_7873",
            "chart_7878",
            "chart_7881",
            "chart_7882",
            "chart_7883",
            "chart_7884",
            "chart_7885",
            "chart_7888",
            "chart_7911",
            "chart_7912",
            "chart_7913",
            "chart_7914",
            "chart_7915",
            "chart_7918",
            "chart_7921",
            "chart_7922",
            "chart_7923",
            "chart_7928",
            "chart_798",
            "chart_811",
            "chart_8121",
            "chart_8122",
            "chart_818",
            "chart_89",
            "pt_chart_template",
        ],
        False,
    )
