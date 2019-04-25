from geopy.distance import distance
import numpy as np

def route(current_pos, beat_list):
	n=len(beat_list)
	f2=beat_list[n-1]
	f1=beat_list[n/2]

	co_ord_1=set()
	co_ord_2=set()
	cop_co_ord=set()
	
	for key,value in f1.items():
		co_ord_1.add(key);co_ord_1.add(value)
	for key,value in f2.items():
		co_ord_2.add(key);co_ord_2.add(value)
	for key,value in current_pos.items():
		cop_co_ord.add(key);cop_co_ord.add(value)

	return distance(cop_co_ord,co_ord_1).km, distance(cop_co_ord,co_ord_2).km, cop_co_ord

#print "Distance between the cop and beat areas : ",route({25:26},[{25:27},{25:29},{25:31},{31:33},{30:34}])

def automate(current_pos, beat_list):
	f1,f2,c_p=route(current_pos,beat_list)
	first_beat,fb=beat_list[0],set()
	
	for k,v in first_beat.items():
		fb.add(k); fb.add(v)

	beat_points = []
	for item in beat_list:
		new_set=set()
		for k,v in item.items():
			new_set.add(k);new_set.add(v)
		beat_points.append(new_set)
	#print "BP : ",beat_points
	
	for item in current_pos:
		key,val=item,current_pos[item]
	#print key,val
	k=0
	for i in np.arange(int(f1),int(f2),1.0):
		if distance(c_p,fb).km == 0:
			print "Beat has started. "
		
		#c_p=update() - update gps long,lat in format {long:lat}
		current_pos[key]+=1; current_pos[key]=current_pos[key]%90.0; c_p.clear(); c_p.add(key); c_p.add(current_pos[key])

		dist = int(distance(c_p, beat_points[k]).km)
		#print dist

		if dist == 0:
			print "Beat point ",k," has been reached."
			k=k+1
		if k==len(beat_points):
			break

automate({25:26},[{25:27},{25:29},{25:31},{31:33},{30:34},{25:37}])
