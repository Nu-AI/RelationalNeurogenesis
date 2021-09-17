using System.Collections;
using System.Collections.Generic;
using JetBrains.Annotations;
using UnityEngine;

public class CameraController : MonoBehaviour {

	public GameObject drone;
	private Vector3 offset;
	public Camera nosecam;
	public Camera asscam;
	
	// Use this for initialization
	void Start () 
	{	
		// Turn ON AssCam
		asscam.enabled = true;
		// Turn OFF NoseCam
		nosecam.enabled = false;
	}
	
	// Update is called once per frame
	void Update()
	{
		if (Input.GetKey(KeyCode.Alpha1))
		{
			// Turn ON NoseCam
			nosecam.enabled = true;
			// Turn OFF AssCam
			asscam.enabled = false;
		}
		if (Input.GetKey(KeyCode.Alpha2))
		{
			// Turn ON AssCam
			asscam.enabled = true;
			// Turn OFF NoseCam
			nosecam.enabled = false;
		}
	}
	
}
