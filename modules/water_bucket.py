from collections import deque

def water_bucket_solver(bucket_x: int, bucket_y: int, bucket_z: int) -> str:
    q = deque([(0, 0, [])])
    seen = set()
    steps = [
        (bucket_x, 0, "Llenar cubo X"),
        (-bucket_x, 0, "Vaciar cubo X"),
        (0, bucket_y, "Llenar cubo Y"),
        (0, -bucket_y, "Vaciar cubo Y"),
        (
            min(bucket_x, bucket_y),
            -min(bucket_x, bucket_y),
            "Transferir del cubo X al Y",
        ),
        (
            -min(bucket_x, bucket_y),
            min(bucket_x, bucket_y),
            "Transferir del cubo Y al X",
        ),
    ]

    while q:
        curX, curY, curSteps = q.popleft()
        for stepX, stepY, action in steps:
            newX, newY = curX + stepX, curY + stepY
            if newX == bucket_z or newY == bucket_z or newX + newY == bucket_z:
                curSteps.append(
                    {
                        "step": len(curSteps) + 1,
                        "bucketX": newX,
                        "bucketY": newY,
                        "action": action,
                        "status": "Solved",
                    }
                )
                return {"Solution": curSteps}
            if (
                (newX, newY) not in seen
                and 0 <= newX <= bucket_x
                and 0 <= newY <= bucket_y
            ):
                seen.add((newX, newY))
                q.append(
                    (
                        newX,
                        newY,
                        curSteps
                        + [
                            {
                                "step": len(curSteps) + 1,
                                "bucketX": newX,
                                "bucketY": newY,
                                "action": action,
                            }
                        ],
                    )
                )
    return {"Solution": ["No Solution"]}
