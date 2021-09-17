using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Windows.Speech;

public class DroneControlManual : MonoBehaviour
{
	private float movespeed;
	private float turnspeed;
	private float liftspeed;
	public GameObject drone;
	private int pitch;
	private int bend;
	
	// Use this for initialization
	void Start ()
	{
		// Get the Rigidbody Component attached to the drone
		//drone = GetComponent<Rigidbody>();

		movespeed = 0.4f;
		liftspeed = 0.2f;
		turnspeed = 50f;

		pitch = 0;
		bend = 0;
	}
	
	// Update is called once per frame
	void Update () 
	{
		if (Input.GetKey(KeyCode.UpArrow))
		{
			// Move the Rigidbody forwards
			transform.Translate(Vector3.forward * movespeed);
			
			// Tilt forward
			if (pitch < 30)
			{
				drone.transform.Rotate(Vector3.right);
				pitch++;	
			}
		}

		else if (Input.GetKey(KeyCode.DownArrow))
		{
			// Move the Rigidbody backwards
			transform.Translate(Vector3.back * movespeed);
			
			// Tilt backward
			if (pitch > -30)
			{
				drone.transform.Rotate(Vector3.left);
				pitch--;	
			}
		}

		else
		{
			// Straighten Out
			if (pitch > 0)
			{
				pitch--;
				drone.transform.Rotate(Vector3.left);
			}
			else if (pitch < 0)
			{
				pitch++;
				drone.transform.Rotate(Vector3.right);
			}
			else
			{
				pitch = 0;
				//drone.transform.localRotation = Quaternion.Euler(0, drone.transform.rotation.y, drone.transform.rotation.z);
			}
		}
		

		if (Input.GetKey(KeyCode.RightArrow))
		{
			// Rotate the sprite about the Y axis in the positive direction
			transform.Rotate(new Vector3(0, 1, 0) * Time.deltaTime * turnspeed);
			
			// Bend rightwards
			if (bend < 30)
			{
				drone.transform.Rotate(Vector3.back);
				bend++;	
			}
		}

		else if (Input.GetKey(KeyCode.LeftArrow))
		{
			// Rotate the sprite about the Y axis in the negative direction
			transform.Rotate(new Vector3(0, -1, 0) * Time.deltaTime * turnspeed);
			
			// Bend leftwards
			if (bend > -30)
			{
				drone.transform.Rotate(Vector3.forward);
				bend--;	
			}
		}

		else
		{
			// Straighten Out
			if (bend > 0)
			{
				bend--;
				drone.transform.Rotate(Vector3.forward);
			}
			else if (bend < 0)
			{
				bend++;
				drone.transform.Rotate(Vector3.back);
			}
			else
			{
				bend = 0;
				//drone.transform.localRotation = Quaternion.Euler(drone.transform.rotation.x, drone.transform.rotation.y, 0);
			}
		}

		if (Input.GetKey(KeyCode.RightShift))
		{
			//Move the Rigidbody upwards constantly at the speed you define
			transform.Translate(Vector3.up * liftspeed);
		}
		
		if (Input.GetKey(KeyCode.RightControl))
		{
			//Move the Rigidbody upwards constantly at the speed you define
			transform.Translate(Vector3.down * liftspeed);
		}
	}
}
