import random

def life_judge(life_my,life_enemy):
	if life_my>0 and life_enemy>0:
		a_end=1
	elif life_my>0 and life_enemy<=0:
		print("敌人失败了")
		a_end=0
	elif life_my<=0 and life_enemy>0:
		print("你失败了")
		a_end=0
	else :
		print("你与敌人同归于尽")
		a_end=0
		return a_end

def velocity_judge(velocity_my,velocity_enemy):
	if velocity_my>velocity_enemy:
		b_end=1
	elif velocity_my<velocity_enemy:
		b_end=0
	else :
		b=random.randint(0,1)
		if b==1:
			b_end=1
		elif b==0:
			b_end=0
	return b_end

def CombatBout_system(life_my,velocity_my,attack_my,defense_my,life_enemy,velocity_enemy,attack_enemy,defense_enemy):
	if velocity_judge(velocity_my,velocity_enemy)==1:
		if attack_my>defense_enemy:
			life_enemy=life_enemy-(attack_my-defense_enemy)
		else :
			life_enemy=life_enemy-1
		if life_enemy<=0:
			print("敌人失败了")
		else :
			if attack_enemy>defense_my:
				life_my=life_my-(attack_enemy-defense_my)
			else :
				life_my=life_my-1
	else :
		if attack_enemy>defense_my:
			life_my=life_my-(attack_enemy-defense_my)
		else :
			life_my=life_my-1
		if life_my<=0:
			print("你失败了")
		else :
			if attack_my>defense_enemy:
				life_enemy=life_enemy-(attack_my-defense_enemy)
			else :
				life_enemy=life_enemy-1

print(CombatBout_system(1,2,1,0,1,3,1,0))