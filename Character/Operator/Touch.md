---
name: Touch
description: 恢复友方单位生命
canUseGeneralPotentialItem: True
canUseActivityPotentialItem: False
potentialItemId: None
activityPotentialItemId: None
classicPotentialItemId: None
nationId: None
groupId: None
teamId: None
displayNumber: None
appellation: Touch
position: RANGED
tagList: ['治疗']
itemUsage: None
itemDesc: None
itemObtainApproach: None
isNotObtainable: True
isSpChar: False
maxPotentialLevel: 0
rarity: TIER_5
profession: MEDIC
subProfessionId: physician
trait: None
phases: [{'characterPrefabKey': 'char_510_amedic', 'rangeId': '3-1', 'maxLevel': 50, 'attributesKeyFrames': [{'level': 1, 'data': {'maxHp': 865, 'atk': 210, 'def': 59, 'magicResistance': 0.0, 'cost': 16, 'blockCnt': 1, 'moveSpeed': 1.0, 'attackSpeed': 100.0, 'baseAttackTime': 2.85, 'respawnTime': 60, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 1.0, 'maxDeployCount': 1, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}, {'level': 50, 'data': {'maxHp': 1219, 'atk': 345, 'def': 86, 'magicResistance': 0.0, 'cost': 16, 'blockCnt': 1, 'moveSpeed': 1.0, 'attackSpeed': 100.0, 'baseAttackTime': 2.85, 'respawnTime': 60, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 1.0, 'maxDeployCount': 1, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}], 'evolveCost': None}, {'characterPrefabKey': 'char_510_amedic', 'rangeId': '3-3', 'maxLevel': 70, 'attributesKeyFrames': [{'level': 1, 'data': {'maxHp': 1219, 'atk': 345, 'def': 86, 'magicResistance': 0.0, 'cost': 18, 'blockCnt': 1, 'moveSpeed': 1.0, 'attackSpeed': 100.0, 'baseAttackTime': 2.85, 'respawnTime': 60, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 1.0, 'maxDeployCount': 1, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}, {'level': 70, 'data': {'maxHp': 1469, 'atk': 493, 'def': 108, 'magicResistance': 0.0, 'cost': 18, 'blockCnt': 1, 'moveSpeed': 1.0, 'attackSpeed': 100.0, 'baseAttackTime': 2.85, 'respawnTime': 60, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 1.0, 'maxDeployCount': 1, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}], 'evolveCost': None}, {'characterPrefabKey': 'char_510_amedic', 'rangeId': '3-3', 'maxLevel': 80, 'attributesKeyFrames': [{'level': 1, 'data': {'maxHp': 1469, 'atk': 493, 'def': 108, 'magicResistance': 0.0, 'cost': 18, 'blockCnt': 1, 'moveSpeed': 1.0, 'attackSpeed': 100.0, 'baseAttackTime': 2.85, 'respawnTime': 60, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 1.0, 'maxDeployCount': 1, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}, {'level': 80, 'data': {'maxHp': 1633, 'atk': 595, 'def': 135, 'magicResistance': 0.0, 'cost': 18, 'blockCnt': 1, 'moveSpeed': 1.0, 'attackSpeed': 100.0, 'baseAttackTime': 2.85, 'respawnTime': 60, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 1.0, 'maxDeployCount': 1, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}], 'evolveCost': None}]
skills: [{'skillId': 'skchr_amedic_1', 'overridePrefabKey': None, 'overrideTokenKey': None, 'levelUpCostCond': [{'unlockCond': {'phase': 'PHASE_2', 'level': 1}, 'lvlUpTime': 0, 'levelUpCost': None}, {'unlockCond': {'phase': 'PHASE_2', 'level': 1}, 'lvlUpTime': 0, 'levelUpCost': None}, {'unlockCond': {'phase': 'PHASE_2', 'level': 1}, 'lvlUpTime': 0, 'levelUpCost': None}], 'unlockCond': {'phase': 'PHASE_0', 'level': 1}}]
displayTokenDict: None
talents: [{'candidates': [{'unlockCondition': {'phase': 'PHASE_1', 'level': 1}, 'requiredPotentialRank': 0, 'prefabKey': '1', 'name': '攫升', 'description': '治疗目标时使其获得+2技力', 'rangeId': None, 'blackboard': [{'key': 'sp', 'value': 2.0, 'valueStr': None}], 'tokenKey': None}, {'unlockCondition': {'phase': 'PHASE_2', 'level': 1}, 'requiredPotentialRank': 0, 'prefabKey': '1', 'name': '攫升', 'description': '治疗目标时使其获得+3技力', 'rangeId': None, 'blackboard': [{'key': 'sp', 'value': 3.0, 'valueStr': None}], 'tokenKey': None}]}]
potentialRanks: []
favorKeyFrames: [{'level': 0, 'data': {'maxHp': 0, 'atk': 0, 'def': 0, 'magicResistance': 0.0, 'cost': 0, 'blockCnt': 0, 'moveSpeed': 0.0, 'attackSpeed': 0.0, 'baseAttackTime': 0.0, 'respawnTime': 0, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 0.0, 'maxDeployCount': 0, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}, {'level': 50, 'data': {'maxHp': 0, 'atk': 0, 'def': 0, 'magicResistance': 0.0, 'cost': 0, 'blockCnt': 0, 'moveSpeed': 0.0, 'attackSpeed': 0.0, 'baseAttackTime': 0.0, 'respawnTime': 0, 'hpRecoveryPerSec': 0.0, 'spRecoveryPerSec': 0.0, 'maxDeployCount': 0, 'maxDeckStackCnt': 0, 'tauntLevel': 0, 'massLevel': 0, 'baseForceLevel': 0, 'stunImmune': False, 'silenceImmune': False, 'sleepImmune': False, 'frozenImmune': False, 'levitateImmune': False}}]
allSkillLvlup: [{'unlockCond': {'phase': 'PHASE_0', 'level': 1}, 'lvlUpCost': None}, {'unlockCond': {'phase': 'PHASE_0', 'level': 1}, 'lvlUpCost': None}, {'unlockCond': {'phase': 'PHASE_0', 'level': 1}, 'lvlUpCost': None}, {'unlockCond': {'phase': 'PHASE_1', 'level': 1}, 'lvlUpCost': None}, {'unlockCond': {'phase': 'PHASE_1', 'level': 1}, 'lvlUpCost': None}, {'unlockCond': {'phase': 'PHASE_1', 'level': 1}, 'lvlUpCost': None}]
---

