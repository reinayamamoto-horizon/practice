class Skill:
    
    # Hero
    HOLY_SLASH = "holy_slash"
    DIVINE_SHIELD = "divine_shield"
    ARCANE_BLADE = "arcane_blade"
    # Warrior
    BERSERKER = 'berserker'
    GUARDISN = 'guardisn'
    WARLORD = 'waelord'
    # Wizard
    ARCHMAGE = "archmage"
    SUMMONER = "summoner"
    CHRONOMANCER = "chronomancer"
    # Priest
    HIGH_PRIEST = "high_priest"
    CLERIC_KNIGHT = "cleric_knight"
    BARD_PRIEST = "bard_priest"

    DATA = {
        # Hero
        HOLY_SLASH: {
            "name":"聖剣ルート",
            "sub_name": "(接近戦アタッカー特化)",
            "power": "攻撃力：★★★★★",
            "defense": "防御：★★★",
            "magic": "魔法：★",
            "speed": "速度：★★★★",
            "description": "聖なる剣撃で敵を斬る",
        },

        DIVINE_SHIELD: {
            "name":"聖騎士ルート",
            "sub_name": "（防御・支援型タンク）",
            "power": "攻撃力：★★★",
            "defense": "防御：★★★★★",
            "magic": "魔法：★★★",
            "speed": "速度：★★",
            "description": "聖なる盾でダメージを軽減",
        },

        ARCANE_BLADE: {
            "name":"魔聖剣ルート",
            "sub_name": "（魔法ハイブリッド）",
            "power": "攻撃力：★★★★",
            "defense": "防御：★★★",
            "magic": "魔法：★★★★",
            "speed": "速度：★★★",
            "description": "魔力をまとった剣撃",
        },

        # Warrior
        BERSERKER: {
            "name":"狂戦士ルート",
            "sub_name": "（火力特化）",
            "power": "攻撃力：★★★★★",
            "defense": "防御：★★",
            "magic": "魔法：★",
            "speed": "速度：★★★★",
            "description": "高火力だが防御が低い",
        },

        GUARDISN: {
            "name":"守護戦士ルート",
            "sub_name": "（タンク）",
            "power": "攻撃力：★★",
            "defense": "防御：★★★★★",
            "magic": "魔法：★",
            "speed": "速度：★★",
            "description": "防御特化の盾役",
        },
        
        WARLORD: {
            "name":"戦術化ルート",
            "sub_name": "（指揮官型）",
            "power": "攻撃力：★★★",
            "defense": "防御：★★★",
            "magic": "魔法：★★",
            "speed": "速度：★★★",
            "description": "戦場指揮型・味方強化",
        },

        # Wizard
        ARCHMAGE:{
            "name":"魔導士ルート",
            "sub_name": "(純粋魔法特化)",
            "power": "攻撃力：★★★★★",
            "defense": "防御：★",
            "magic": "魔法：★★★★★",
            "speed": "速度：★★★",
            "description": "広範囲魔法と高威力魔法を扱う",
        },

        SUMMONER:{
            "name":"召喚士ルート",
            "sub_name": "(召喚獣で戦闘)",
            "power": "攻撃力：★★★",
            "defense": "防御：★★",
            "magic": "魔法：★★★★★",
            "speed": "速度：★★★",
            "description": "召喚獣を使って戦う戦術型",
        },

        CHRONOMANCER:{
            "name":"呪術ルート",
            "sub_name": "(特殊サポート)",
            "power": "攻撃力：★★",
            "defense": "防御：★★",
            "magic": "魔法：★★★★",
            "speed": "速度：★★★★★",
            "description": "精神魔法による戦闘操作",
        },

        # Priest
        HIGH_PRIEST: {
            "name":"呪術ルート",
            "sub_name": "(特殊サポート)",
            "power": "攻撃力：★",
            "defense": "防御：★★★",
            "magic": "魔法：★★★★★",
            "speed": "速度：★★★",
            "description": "回復と浄化に特化",
        },

        CLERIC_KNIGHT: {
            "name":"呪術ルート",
            "sub_name": "(特殊サポート)",
            "power": "攻撃力：★★★",
            "defense": "防御：★★★★",
            "magic": "魔法：★★★",
            "speed": "速度：★★★",
            "description": "前線で戦える僧侶",
        },

        BARD_PRIEST: {
            "name":"呪術ルート",
            "sub_name": "(特殊サポート)",
            "power": "攻撃力：★",
            "defense": "防御：★★",
            "magic": "魔法：★★★★",
            "speed": "速度：★★★★",
            "description": "味方強化特化・バフ",
        },

    }