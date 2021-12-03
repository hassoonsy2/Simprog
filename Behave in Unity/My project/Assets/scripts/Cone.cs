using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class Cone
{
    static List<Collider> result = new List<Collider>();
    static Collider[] overlapping;
    static Plane[] planes = new Plane[6];
    static Vector3 boxCenter;
    static Vector3 halfExtents;

    public static List<Collider> OverlapCone(Vector3 origin, Quaternion rotation, Vector3 scale, float maxDistance, float fovAngle, float aspect, int layerMask)
    {
        halfExtents.z = maxDistance * .5f;
        halfExtents.y = Mathf.Tan(Mathf.Deg2Rad * fovAngle * .5f) * maxDistance;
        halfExtents.x = halfExtents.y * aspect;

        boxCenter = origin + (rotation * Vector3.forward) * .5f * maxDistance;
        overlapping = Physics.OverlapBox(boxCenter, halfExtents, rotation, layerMask);

        GeometryUtility.CalculateFrustumPlanes(Matrix4x4.Perspective(fovAngle, aspect, 0f, maxDistance), planes);

        result.Clear();
        foreach (Collider collider in overlapping)
        {
            if (GeometryUtility.TestPlanesAABB(planes, collider.bounds))
            {
                result.Add(collider);
            }
        }

        return result;
    }

    public static List<Collider> OverlapCone(Camera camera, Vector3 origin, Quaternion rotation, Vector3 scale, float maxDistance, float fovAngle, float aspect, int layerMask)
    {
        halfExtents.z = maxDistance * .5f;
        halfExtents.y = Mathf.Tan(Mathf.Deg2Rad * fovAngle * .5f) * maxDistance;
        halfExtents.x = halfExtents.y * aspect;

        boxCenter = origin + (rotation * Vector3.forward) * .5f * maxDistance;
        overlapping = Physics.OverlapBox(boxCenter, halfExtents, rotation, layerMask);

        GeometryUtility.CalculateFrustumPlanes(camera, planes);

        result.Clear();
        foreach (Collider collider in overlapping)
        {
            if (GeometryUtility.TestPlanesAABB(planes, collider.bounds))
            {
                result.Add(collider);
            }
        }

        return result;
    }
}