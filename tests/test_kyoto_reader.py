from typing import List, Dict

from kyoto_reader import KyotoReader, Mention, Entity, Predicate, SpecialArgument, Argument


def test_pas(fixture_kyoto_reader: KyotoReader):
    document = fixture_kyoto_reader.process_document('w201106-0000060050')
    predicates: List[Predicate] = document.get_predicates()
    assert len(predicates) == 12

    sid1 = 'w201106-0000060050-1'
    sid2 = 'w201106-0000060050-2'
    sid3 = 'w201106-0000060050-3'

    arguments = document.get_arguments(predicates[0])
    assert predicates[0].midasi == 'トスを'
    assert len([_ for args in arguments.values() for _ in args]) == 2
    arg = arguments['ガ'][0]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('不特定:人', [0], 'exo', '')
    arg = arguments['ヲ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('コイン', 0, 0, sid1, [1], 'dep', '')

    arguments = document.get_arguments(predicates[1])
    assert predicates[1].midasi == '行う。'
    assert len([_ for args in arguments.values() for _ in args]) == 4
    arg = arguments['ガ'][0]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('不特定:人', [2], 'exo', '')
    arg = arguments['ガ'][1]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('読者', [3], 'exo', '？')
    arg = arguments['ガ'][2]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('著者', [4], 'exo', '？')
    arg = arguments['ヲ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('トス', 1, 1, sid1, [5], 'overt', '')

    arguments = document.get_arguments(predicates[2])
    assert predicates[2].midasi == '表が'
    assert len([_ for args in arguments.values() for _ in args]) == 1
    arg = arguments['ノ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('コイン', 0, 0, sid1, [1], 'inter', '')

    arguments = document.get_arguments(predicates[3])
    assert predicates[3].midasi == '出た'
    assert len([_ for args in arguments.values() for _ in args]) == 2
    arg = arguments['ガ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('表', 0, 4, sid2, [6], 'overt', '')
    arg = arguments['外の関係'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('数', 2, 6, sid2, [7], 'dep', '')

    arguments = document.get_arguments(predicates[4])
    assert predicates[4].midasi == '数だけ、'
    assert len([_ for args in arguments.values() for _ in args]) == 1
    arg = arguments['ノ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('出た', 1, 5, sid2, [8], 'dep', '')

    arguments = document.get_arguments(predicates[5])
    assert predicates[5].midasi == 'モンスターを'
    assert len([_ for args in arguments.values() for _ in args]) == 2
    arg = arguments['修飾'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('フィールド上', 3, 7, sid2, [9], 'dep', '')
    arg = arguments['修飾'][1]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('数', 2, 6, sid2, [7], 'intra', 'AND')

    arguments = document.get_arguments(predicates[6])
    assert predicates[6].midasi == '破壊する。'
    assert len([_ for args in arguments.values() for _ in args]) == 2
    arg = arguments['ガ'][0]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('不特定:状況', [11], 'exo', '')
    arg = arguments['ヲ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('モンスター', 4, 8, sid2, [10], 'overt', '')

    arguments = document.get_arguments(predicates[7])
    assert predicates[7].midasi == '効果は'
    assert len([_ for args in arguments.values() for _ in args]) == 1
    arg = arguments['トイウ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('破壊する', 5, 9, sid2, [12], 'inter', '')

    arguments = document.get_arguments(predicates[8])
    assert predicates[8].midasi == '１度だけ'
    assert len([_ for args in arguments.values() for _ in args]) == 1
    arg = arguments['ニ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('ターン', 3, 13, sid3, [13], 'overt', '')

    arguments = document.get_arguments(predicates[9])
    assert predicates[9].midasi == 'メイン'
    assert len([_ for args in arguments.values() for _ in args]) == 1
    arg = arguments['ガ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('フェイズ', 7, 17, sid3, [15], 'dep', '')

    arguments = document.get_arguments(predicates[10])
    assert predicates[10].midasi == 'フェイズに'
    assert len([_ for args in arguments.values() for _ in args]) == 1
    arg = arguments['ノ？'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('自分', 5, 15, sid3, [3, 4, 14], 'overt', '')

    arguments = document.get_arguments(predicates[11])
    assert predicates[11].midasi == '使用する事ができる。'
    assert len([_ for args in arguments.values() for _ in args]) == 5
    arg = arguments['ガ'][0]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('不特定:人', [16], 'exo', '')
    arg = arguments['ガ'][1]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('著者', [4], 'exo', '？')
    arg = arguments['ガ'][2]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('読者', [3], 'exo', '？')
    arg = arguments['ヲ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('効果', 1, 11, sid3, [17], 'dep', '')
    arg = arguments['ニ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('フェイズ', 7, 17, sid3, [15], 'overt', '')


def test_pas_relax1(fixture_kyoto_reader: KyotoReader):
    document = fixture_kyoto_reader.process_document('w201106-0000060050')
    predicates: List[Predicate] = document.get_predicates()
    arguments = document.get_arguments(predicates[10], relax=True)
    sid3 = 'w201106-0000060050-3'
    assert predicates[10].midasi == 'フェイズに'
    assert len([_ for args in arguments.values() for _ in args]) == 4
    args = sorted(arguments['ノ？'], key=lambda a: a.midasi)
    assert isinstance(args[0], SpecialArgument)
    assert tuple(args[0]) == ('不特定:人', [14], 'exo', 'AND')
    assert isinstance(args[1], Argument)
    assert tuple(args[1]) == ('自分', 5, 15, sid3, [3, 4, 14], 'overt', '')
    assert isinstance(args[2], SpecialArgument)
    assert tuple(args[2]) == ('著者', [4], 'exo', 'AND')
    assert isinstance(args[3], SpecialArgument)
    assert tuple(args[3]) == ('読者', [3], 'exo', 'AND')


def test_pas_relax2(fixture_kyoto_reader: KyotoReader):
    document = fixture_kyoto_reader.process_document('w201106-0000060560')
    predicates: List[Predicate] = document.get_predicates()
    arguments = document.get_arguments(predicates[9], relax=True)
    sid1 = 'w201106-0000060560-1'
    sid2 = 'w201106-0000060560-2'
    sid3 = 'w201106-0000060560-3'
    assert predicates[9].midasi == 'ご協力の'
    assert len([_ for args in arguments.values() for _ in args]) == 6
    arg = arguments['ガ'][0]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('皆様', 1, 17, sid3, [14], 'intra', '')
    arg = arguments['ガ'][1]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('ドクターの', 0, 16, sid3, [14], 'intra', 'AND')
    arg = arguments['ガ'][2]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('ドクターを', 2, 11, sid2, [14], 'inter', 'AND')
    arg = arguments['ガ'][3]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('ドクターを', 7, 7, sid1, [14], 'inter', 'AND')
    arg = arguments['ニ'][0]
    assert isinstance(arg, SpecialArgument)
    assert tuple(arg) == ('著者', [5], 'exo', '')
    arg = arguments['ニ'][1]
    assert isinstance(arg, Argument)
    assert tuple(arg) == ('コーナー', 5, 14, sid2, [11], 'inter', '？')


def test_coref1(fixture_kyoto_reader: KyotoReader):
    document = fixture_kyoto_reader.process_document('w201106-0000060050')
    entities: Dict[int, Entity] = document.entities
    assert len(entities) == 18

    entity = entities[0]
    assert (entity.taigen, entity.yougen) == (None, None)
    assert entity.exophor == '不特定:人'
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 0

    entity = entities[1]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('コイン', 0)
    assert mentions[0].eids == {1}

    entity = entities[2]
    assert (entity.taigen, entity.yougen) == (None, None)
    assert entity.exophor == '不特定:人'
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 0

    entity = entities[3]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor == '読者'
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('自分の', 15)
    assert mentions[0].eids == {3, 4, 14}

    entity = entities[4]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor == '著者'
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('自分の', 15)
    assert mentions[0].eids == {3, 4, 14}

    entity = entities[5]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('トスを', 1)
    assert mentions[0].eids == {5}

    entity = entities[6]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('表が', 4)
    assert mentions[0].eids == {6}

    entity = entities[7]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('数だけ、', 6)
    assert mentions[0].eids == {7}

    entity = entities[8]
    assert (entity.taigen, entity.yougen) == (False, True)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('出た', 5)
    assert mentions[0].eids == {8}

    entity = entities[9]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('フィールド上の', 7)
    assert mentions[0].eids == {9}

    entity = entities[10]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('モンスターを', 8)
    assert mentions[0].eids == {10}

    entity = entities[11]
    assert (entity.taigen, entity.yougen) == (None, None)
    assert entity.exophor == '不特定:状況'
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 0

    entity = entities[12]
    assert (entity.taigen, entity.yougen) == (False, True)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('破壊する。', 9)
    assert mentions[0].eids == {12}

    entity = entities[13]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('ターンに', 13)
    assert mentions[0].eids == {13}

    entity = entities[14]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor == '不特定:人'
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('自分の', 15)
    assert mentions[0].eids == {3, 4, 14}

    entity = entities[15]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('フェイズに', 17)
    assert mentions[0].eids == {15}

    entity = entities[16]
    assert (entity.taigen, entity.yougen) == (None, None)
    assert entity.exophor == '不特定:人'
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 0

    entity = entities[17]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 1
    assert (mentions[0].midasi, mentions[0].dtid) == ('効果は', 11)
    assert mentions[0].eids == {17}


def test_coref2(fixture_kyoto_reader: KyotoReader):
    document = fixture_kyoto_reader.process_document('w201106-0000060560')
    entities: Dict[int, Entity] = document.entities
    assert len(entities) == 14

    entity: Entity = entities[14]
    assert (entity.taigen, entity.yougen) == (True, False)
    assert entity.exophor is None
    mentions: List[Mention] = sorted(entity.mentions, key=lambda x: x.dtid)
    assert len(mentions) == 4
    assert (mentions[0].midasi, mentions[0].dtid, mentions[0].eids) == ('ドクターを', 7, {14})
    assert (mentions[1].midasi, mentions[1].dtid, mentions[1].eids) == ('ドクターを', 11, {14})
    assert (mentions[2].midasi, mentions[2].dtid, mentions[2].eids) == ('ドクターの', 16, {14})
    assert (mentions[3].midasi, mentions[3].dtid, mentions[3].eids) == ('皆様', 17, {14})


def test_ne(fixture_kyoto_reader: KyotoReader):
    document = fixture_kyoto_reader.process_document('w201106-0000060877')
    nes = document.named_entities
    assert len(nes) == 2
    ne = nes[0]
    assert (ne.category, ne.midasi, ne.dmid_range) == ('ORGANIZATION', '柏市ひまわり園', range(5, 9))
    ne = nes[1]
    assert (ne.category, ne.midasi, ne.dmid_range) == ('DATE', '平成２３年度', range(11, 14))

    document = fixture_kyoto_reader.process_document('w201106-0000074273')
    nes = document.named_entities
    assert len(nes) == 3
    ne = nes[0]
    assert (ne.category, ne.midasi, ne.dmid_range) == ('LOCATION', 'ダーマ神殿', range(15, 17))
    ne = nes[1]
    assert (ne.category, ne.midasi, ne.dmid_range) == ('ARTIFACT', '天の箱舟', range(24, 27))
    ne = nes[2]
    assert (ne.category, ne.midasi, ne.dmid_range) == ('LOCATION', 'ナザム村', range(39, 41))
