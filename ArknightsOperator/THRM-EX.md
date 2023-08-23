---
name: THRM-EX
description: 不进行攻击，且不受<@ba.kw>部署数量</>限制，但再部署时间极长
canUseGeneralPotentialItem: False
canUseActivityPotentialItem: False
potentialItemId: p_char_376_therex
activityPotentialItemId: None
classicPotentialItemId: None
nationId: rhodes
groupId: None
teamId: None
displayNumber: RCX4
appellation: Thermal-EX
position: MELEE
tagList: ['支援机械', '爆发']
itemUsage: 罗德岛特种机器人Thermal-EX（亦作THRM-EX），被工程师可露希尔派来执行战地作战任务。
itemDesc: 他知道自己是一台机器人。
itemObtainApproach: 招募寻访
isNotObtainable: False
isSpChar: False
maxPotentialLevel: 5
rarity: TIER_1
profession: SPECIAL
subProfessionId: executor
trait: None
phases: [{'characterPrefabKey': 'char_376_therex', 'rangeId': 'x-4', 'maxLevel': 30, 'attributesKeyFrames': [{'level': 1, 'data': {'maxHp': 1154, 'atk': 208, 'def': 354, 'magicResistance': 50.0, 'cost': 3, 'blockCnt': 0, 'moveSpeed': 1.0, 'attackSpeed': 100.0, 'baseAttackTime': 0.93, 'respawnTime': 200, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 1.0, 'maxDeployCount': 1, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}, {'level': 30, 'data': {'maxHp': 1443, 'atk': 260, 'def': 443, 'magicResistance': 50.0, 'cost': 3, 'blockCnt': 0, 'moveSpeed': 1.0, 'attackSpeed': 100.0, 'baseAttackTime': 0.93, 'respawnTime': 200, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 1.0, 'maxDeployCount': 1, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}], 'evolveCost': None}]
skills: []
displayTokenDict: None
talents: [{'candidates': [{'unlockCondition': {'phase': 'PHASE_0', 'level': 1}, 'requiredPotentialRank': 0, 'prefabKey': '1', 'name': '延迟引爆·I', 'description': '部署经过3秒后，对周围8格内的所有敌人造成相当于攻击力300%的物理伤害，并令其获得8秒10%的<$ba.fragile>脆弱</>效果，之后自身强制退出战场', 'rangeId': None, 'blackboard': [{'key': 'interval', 'value': 3.0, 'valueStr': None}, {'key': 'damage_by_atk_scale', 'value': 3.0, 'valueStr': None}, {'key': 'weak[limit]', 'value': 8.0, 'valueStr': None}, {'key': 'damage_scale', 'value': 1.1, 'valueStr': None}], 'tokenKey': None}, {'unlockCondition': {'phase': 'PHASE_0', 'level': 1}, 'requiredPotentialRank': 1, 'prefabKey': '1', 'name': '延迟引爆·II', 'description': '部署经过3秒后，对周围8格内的所有敌人造成相当于攻击力320%的物理伤害，并令其获得8秒18%的<$ba.fragile>脆弱</>效果，之后自身强制退出战场', 'rangeId': None, 'blackboard': [{'key': 'interval', 'value': 3.0, 'valueStr': None}, {'key': 'damage_by_atk_scale', 'value': 3.2, 'valueStr': None}, {'key': 'weak[limit]', 'value': 8.0, 'valueStr': None}, {'key': 'damage_scale', 'value': 1.18, 'valueStr': None}], 'tokenKey': None}, {'unlockCondition': {'phase': 'PHASE_0', 'level': 1}, 'requiredPotentialRank': 2, 'prefabKey': '1', 'name': '延迟引爆·III', 'description': '部署经过3秒后，对周围8格内的所有敌人造成相当于攻击力340%的物理伤害，并令其获得8秒21%的<$ba.fragile>脆弱</>效果，之后自身强制退出战场', 'rangeId': None, 'blackboard': [{'key': 'interval', 'value': 3.0, 'valueStr': None}, {'key': 'damage_by_atk_scale', 'value': 3.4, 'valueStr': None}, {'key': 'weak[limit]', 'value': 8.0, 'valueStr': None}, {'key': 'damage_scale', 'value': 1.21, 'valueStr': None}], 'tokenKey': None}, {'unlockCondition': {'phase': 'PHASE_0', 'level': 1}, 'requiredPotentialRank': 3, 'prefabKey': '1', 'name': '延迟引爆·IV', 'description': '部署经过3秒后，对周围8格内的所有敌人造成相当于攻击力360%的物理伤害，并令其获得8秒24%的<$ba.fragile>脆弱</>效果，之后自身强制退出战场', 'rangeId': None, 'blackboard': [{'key': 'interval', 'value': 3.0, 'valueStr': None}, {'key': 'damage_by_atk_scale', 'value': 3.6, 'valueStr': None}, {'key': 'weak[limit]', 'value': 8.0, 'valueStr': None}, {'key': 'damage_scale', 'value': 1.24, 'valueStr': None}], 'tokenKey': None}, {'unlockCondition': {'phase': 'PHASE_0', 'level': 1}, 'requiredPotentialRank': 4, 'prefabKey': '1', 'name': '延迟引爆·V', 'description': '部署经过3秒后，对周围8格内的所有敌人造成相当于攻击力380%的物理伤害，并令其获得8秒27%的<$ba.fragile>脆弱</>效果，之后自身强制退出战场', 'rangeId': None, 'blackboard': [{'key': 'interval', 'value': 3.0, 'valueStr': None}, {'key': 'damage_by_atk_scale', 'value': 3.8, 'valueStr': None}, {'key': 'weak[limit]', 'value': 8.0, 'valueStr': None}, {'key': 'damage_scale', 'value': 1.27, 'valueStr': None}], 'tokenKey': None}, {'unlockCondition': {'phase': 'PHASE_0', 'level': 1}, 'requiredPotentialRank': 5, 'prefabKey': '1', 'name': '延迟引爆·VI', 'description': '部署经过3秒后，对周围8格内的所有敌人造成相当于攻击力400%的物理伤害，并令其获得8秒30%的<$ba.fragile>脆弱</>效果，之后自身强制退出战场', 'rangeId': None, 'blackboard': [{'key': 'interval', 'value': 3.0, 'valueStr': None}, {'key': 'damage_by_atk_scale', 'value': 4.0, 'valueStr': None}, {'key': 'weak[limit]', 'value': 8.0, 'valueStr': None}, {'key': 'damage_scale', 'value': 1.3, 'valueStr': None}], 'tokenKey': None}]}]
potentialRanks: [{'type': 'CUSTOM', 'description': '天赋效果加强', 'buff': None, 'equivalentCost': None}, {'type': 'CUSTOM', 'description': '天赋效果加强', 'buff': None, 'equivalentCost': None}, {'type': 'CUSTOM', 'description': '天赋效果加强', 'buff': None, 'equivalentCost': None}, {'type': 'CUSTOM', 'description': '天赋效果加强', 'buff': None, 'equivalentCost': None}, {'type': 'CUSTOM', 'description': '天赋效果加强', 'buff': None, 'equivalentCost': None}]
favorKeyFrames: [{'level': 0, 'data': {'maxHp': 0, 'atk': 0, 'def': 0, 'magicResistance': 0.0, 'cost': 0, 'blockCnt': 0, 'moveSpeed': 0.0, 'attackSpeed': 0.0, 'baseAttackTime': 0.0, 'respawnTime': 0, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 0.0, 'maxDeployCount': 0, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}, {'level': 50, 'data': {'maxHp': 0, 'atk': 90, 'def': 0, 'magicResistance': 0.0, 'cost': 0, 'blockCnt': 0, 'moveSpeed': 0.0, 'attackSpeed': 0.0, 'baseAttackTime': 0.0, 'respawnTime': 0, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 0.0, 'maxDeployCount': 0, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}]
allSkillLvlup: []
---

