using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class AgentSocket : MonoBehaviour 
{
	public TCPTestClient mySocket;
	public Camera cam;
	public NavMeshAgent agent;

	// Use this for initialization
	void Start () 
	{

	}
	
	// Update is called once per frame
	void Update () 
	{
		if(Input.GetMouseButtonDown(0))
		{
			Ray ray = cam.ScreenPointToRay(Input.mousePosition);
			RaycastHit hit;

			if(Physics.Raycast(ray, out hit))
			{
				// Move Our Agent
				// agent.SetDestination(hit.point);
				mySocket.SendData(hit.point.ToString("G4"));
			}
		}
	}
}
