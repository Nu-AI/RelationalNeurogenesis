using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DroneBladeSpin : MonoBehaviour 
{

	// Use this for initialization
	void Start () 
	{
		
	}
	
	// Update is called once per frame
	void Update () 
	{
		// Rotate the object around its local Z axis at 1 degree per second
		transform.Rotate(Vector3.forward, 50000* Time.deltaTime);
	}
}
