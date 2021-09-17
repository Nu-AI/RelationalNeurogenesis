using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DroneDrift : MonoBehaviour 
{

	private float amplitudeY1 = 0.001f;
	private float amplitudeY2 = 0.003f;
	private float amplitudeY3 = -0.005f;
	private float omegaY1 = 1.33f;
	private float omegaY2 = 1.2f;
	private float omegaY3 = 1.3f;
	float index;
	
	// Use this for initialization
	void Start ()
	{
		index = 0;
	}
	
	// Update is called once per frame
	void Update () 
	{
		index += Time.deltaTime;
		//float x = amplitudeX*Mathf.Cos (omegaX*index);
		float y1 = amplitudeY1 * Mathf.Sin (omegaY1 * index);
		float y2 = amplitudeY2 * Mathf.Sin (omegaY2 * index);
		float y3 = amplitudeY3 * Mathf.Sin (omegaY3 * index);
		
		transform.Translate((y1 + y2 + y3) * Vector3.up);
	}
}
