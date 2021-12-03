using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sight : MonoBehaviour
{
    [SerializeField] float angle = 60f;
    [SerializeField] float distance = 20f;
    [SerializeField] float aspect = 2f;
    [SerializeField] Color gizmocolor = Color.red;
    [SerializeField] LayerMask layerMask;
    HashSet<Collider> inSight, lastInSight;


    Collider[] overlaps;

   
    void Awake()
    {
        inSight = new HashSet<Collider>();
        
    }
    RaycastHit hitInfo;

    void Fixedupdate()
    {
        lastInSight = new HashSet<Collider>(inSight);
        overlaps = Physics.OverlapSphere(transform.position, distance, layerMask);
        foreach (Collider collider in overlaps)

        {
            if(Physics.Raycast(transform.position, collider.transform.position - transform.position, out hitInfo, distance, layerMask)
                && hitInfo.collider == collider)
            {
                if (!inSight.Contains(collider))
                {
                    inSight.Add(collider);
                    Debug.Log($"Sighted : {collider.gameObject.name}");
                }

                else
                {
                    lastInSight.Remove(collider);
                }
            }
        }

        foreach (Collider collider in lastInSight)
        {
            inSight.Remove(collider);
            Debug.Log($"No Longer seeing : {collider.gameObject.name}");


        }
    }

    void OnDrawGizmos()
    {
        if (inSight != null)
        {
            Gizmos.color = Color.magenta;
            foreach (Collider collider in inSight)
            {
                Gizmos.DrawLine(transform.position, collider.transform.position);
            }
        }
        
        Gizmos.color = gizmocolor;
        
        Gizmos.matrix = Matrix4x4.TRS(transform.position, transform.rotation, transform.lossyScale);
        Gizmos.DrawFrustum(Vector3.zero, angle, distance, .5f, aspect);

    }

}
