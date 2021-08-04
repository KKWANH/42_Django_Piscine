import sys
import antigravity

def	ft_main():
	if len(sys.argv) == 4:
		try:
			latitude = float(sys.argv[1])
			longitude = float(sys.argv[2])
		except:
			return print("argv[1] or [2] required type: float")
		try:
			datedow = sys.argv[3].encode('utf-8')
		except:
			return print("argv[3] requires type: string")
		antigravity.geohash(latitude, longitude, datedow)
	else:
		print("3 Arguments required. (float, float, string)")

if __name__ == '__main__':
    ft_main()
