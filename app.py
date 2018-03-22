from flask import Flask,jsonify,json,Response
import psycopg2

app = Flask(__name__)

@app.route("/recommend/<id>/")
def recomend(id):
	conn=psycopg2.connect(host='ec2-54-197-250-121.compute-1.amazonaws.com',database='d8ruqq5kb8v79r',user='iymhmnwfijgaso',password='7d5ffd1e6f2e1a42ba631a9f271910afc7beb8661e980b56da5472749b99321e')
	cur=conn.cursor()
	cur.execute('''SELECT * FROM reco2 WHERE id_movie='''+str(id))
	rows=cur.fetchall()
	conn.close()
	recolist=[{'Movie of interest':{'Id':rows[0][0],'Movie name':rows[0][1]}}]
	for i in range(5):
		recodict={'Recommendation_'+str(i+1):{'Id':rows[0][2*i+2],'Movie name':rows[0][2*i+3]}}
		recolist.append(recodict)
	jsonStr=json.dumps(recolist)
	return(Response(response=jsonStr,status=200,mimetype='application/json'))
	
	
if __name__ == '__main__':
    app.run(debug=True)
