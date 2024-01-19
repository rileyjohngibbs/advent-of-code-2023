'use client'

import { useEffect, useState } from "react"

export default function SolutionStepper({ inputLines }: { inputLines: string[] }) {
    const [loop, setLoop] = useState<[number, number][]>()
    const [solution, setSolution] = useState<number>()
    const loopSet = new Set((loop || []).map(([y, x]) => `${y},${x}`))

    useEffect(() => {
        if (!loop) {
            setTimeout(() => setLoop([findAnimal(inputLines)]), 1000)
        } else if (loop.length === 1) {
            const [ay, ax] = loop[0]
            const connectedToAnimal = (y: number, x: number) => (
                getConnections(y, x, inputLines[y][x]).find(
                    addr => addressEqual(addr, [ay, ax])
                ) !== undefined
            )
            const neighbors: [number, number][] = [[ay - 1, ax], [ay + 1, ax], [ay, ax - 1], [ay, ax + 1]]
            const nextPipe = neighbors.find(([y, x]) => connectedToAnimal(y, x))
            if (!nextPipe) throw "no pipe connected to animal"
            setTimeout(() => setLoop([...loop, nextPipe]), 1000)
        } else if (!addressEqual(loop[loop.length - 1], loop[0])) {
            const nextLoop = Array(91).fill(null).reduce<[number, number][]>(
                (agg, _) => {
                    const [y, x] = agg[agg.length - 1]
                    const pipe = getConnections(y, x, inputLines[y][x]).filter(
                        addr => !addressEqual(addr, agg[agg.length - 2])
                    )[0]
                    return pipe ? [...agg, pipe] : agg
                },
                loop
            )
            if (addressEqual(nextLoop[nextLoop.length - 1], nextLoop[0])) {
                setTimeout(() => setLoop(nextLoop.slice(0, nextLoop.length - 1)), 10)
                setTimeout(() => setSolution(nextLoop.length / 2), 1000)
            } else {
                setLoop(nextLoop)
            }
        }
    }, [loop])

    return <div className="flex flex-col">
        <div>Loop Length: {loop?.length} Farthest Point: {solution === undefined ? "" : solution}</div>
        {inputLines.map((line, y) => <div className="flex flex-row" key={y}>{
            line.split("").map((point, x) => {
                let className: string = ""
                let backgroundImage: string = ""
                if (loopSet.has(`${y},${x}`)) {
                    const img = point === "S" ? "" : pipe_svg(point)
                    className = `font-bold ${img} bg-center bg-cover`
                    backgroundImage = `url("/images/${img}.svg")`
                }
                return <div key={x} className={className} style={{backgroundImage}}>
                    {point}
                </div>
            })
        }</div>)}
    </div>
}

const findAnimal = (inputLines: string[]): [number, number] => {
    for (let y = 0; y < inputLines.length; y++) {
        const sx = inputLines[y].indexOf("S")
        if (sx !== -1) return [y, sx]
    }
    throw "no animal found"
}

const getConnections = (y: number, x: number, pipe: string): [number, number][] => {
    switch (pipe) {
        case "L":
            return [[y - 1, x], [y, x + 1]]
        case "J":
            return [[y - 1, x], [y, x - 1]]
        case "7":
            return [[y, x - 1], [y + 1, x]]
        case "F":
            return [[y, x + 1], [y + 1, x]]
        case "|":
            return [[y - 1, x], [y + 1, x]]
        case "-":
            return [[y, x - 1], [y, x + 1]]
        default:
            return []
    }
}

const addressEqual = (addr1: number[], addr2: number[]) => {
    return addr1[0] == addr2[0] && addr1[1] == addr2[1]
}

const pipe_svg = (pipe: string) => {
    switch (pipe) {
        case "|": return "v-pipe"
        case "-": return "h-pipe"
        case "7": return "7-pipe"
        case "J": return "J-pipe"
        case "L": return "L-pipe"
        case "F": return "F-pipe"
        default: throw "no fair"
    }
}