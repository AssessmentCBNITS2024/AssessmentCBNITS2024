from flask import Flask, request, jsonify
import sys
sys.path.append(r"<relative_path>/Palo_alto_Folder")
from Function_Calls.app import Auth0Client

app = Flask(__name__)

auth0_domain = "test-auth0-domain"
api_token = "test-auth0-management-api-token"

auth0_client = Auth0Client(auth0_domain, api_token)

@app.route('/users', methods=['GET'])
def getUser():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    user = auth0_client.getUser(user_id)
    return jsonify(user)

@app.route('/users', methods=['POST'])
def createUser():
    user_data = request.json
    if not user_data:
        return jsonify({"error": "User data is required"}), 400
    created_user = auth0_client.createUser(user_data)
    return jsonify(created_user), 201

@app.route('/users', methods=['DELETE'])
def deleteUser():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    deletion_status = auth0_client.deleteUser(user_id)
    return jsonify({"status": "success" if deletion_status == 204 else "failed"}), deletion_status

if __name__ == '__main__':
    app.run(port=5000, debug=True)
