using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VisionEventArgs
{
    public Collider collider;
}

public class Sight : MonoBehaviour
{
    [SerializeField] private Camera camera;

    private const Modality MODALITY = Modality.SIGHT;
    [SerializeField] private float angle = 60f;
    [SerializeField] private float distance = 50f;
    [SerializeField] private float aspect = 2f;
    [SerializeField] private Color gizmoColor = Color.red;
    [SerializeField] private LayerMask layerMask;
    internal HashSet<Collider> inSight;
    private HashSet<Collider> lastInSight;
    private float coneRadius;

    public delegate void VisionEventHandler(object sender, VisionEventArgs args);
    public event VisionEventHandler OnEnterVision, OnLeaveVision;

    void Awake()
    {
        inSight = new HashSet<Collider>();
        coneRadius = Mathf.Tan(Mathf.Deg2Rad * angle / 2f) * distance;
    }

    private RaycastHit hitInfo;
    // private RaycastHit[] coneHits;
    private Collider coneHitCollider;
    private List<Collider> overlaps;

    void FixedUpdate()
    {
        lastInSight = new HashSet<Collider>(inSight);

        overlaps = Cone.OverlapCone(camera, transform.position, transform.rotation, transform.lossyScale, distance, angle, aspect, layerMask);
        foreach (Collider coneHitCollider in overlaps)
        // coneHits = ConeCast.ConeCastAll(transform.position, coneRadius, transform.forward, distance, angle);
        // foreach (RaycastHit coneHit in coneHits)
        {
            // coneHitCollider = coneHit.collider;
            if (Physics.Raycast(transform.position, coneHitCollider.transform.position - transform.position, out hitInfo, distance, layerMask)
                && hitInfo.collider == coneHitCollider)
            {
                if (!inSight.Contains(coneHitCollider))
                {
                    inSight.Add(coneHitCollider);
                    OnEnterVision.Invoke(this, new VisionEventArgs() { collider = coneHitCollider });

                }
                else
                {
                    lastInSight.Remove(coneHitCollider);
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

        Gizmos.color = Color.red;
        Gizmos.matrix = Matrix4x4.TRS(transform.position, transform.rotation, transform.lossyScale);
        Gizmos.DrawFrustum(Vector3.zero, angle, distance, .5f, aspect);
    }
}