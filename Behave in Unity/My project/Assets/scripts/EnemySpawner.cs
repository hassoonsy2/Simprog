using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemySpawner : MonoBehaviour
{
    private float timer = 0f;
    [SerializeField] private float spawnTime = 1f;
    [SerializeField] private GameObject enemyPrefab;
    private int numEnemies = 0;
    [SerializeField] int maxEnemies = 20;

    // Update is called once per frame
    void FixedUpdate()
    {

        if (numEnemies < maxEnemies)
        {
            timer += Time.fixedDeltaTime;
            if (timer >= spawnTime)
            {
                timer -= spawnTime;
                Vector2 circlePosition = Random.insideUnitCircle.normalized * 20f;
                //Spawn Enemy
                Instantiate(enemyPrefab, new Vector3(circlePosition.x, 1f, circlePosition.y), Quaternion.identity).name = $"Enemy {++numEnemies}";
            }
        }
    }
}