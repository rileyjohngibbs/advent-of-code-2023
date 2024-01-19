'use client'

import { useEffect, useState } from "react"
import UnsolvedStack from "./UnsolvedStack"

export default function SolutionStepper({ inputLines }: { inputLines: string[] }) {
    const [parsedLines, _] = useState(inputLines.map(parseLine))
    const [historyStacks, setHistoryStacks] = useState<number[][][]>([[parsedLines[0]]])
    const [solution, setSolution] = useState<number[]>()

    useEffect(() => {
        const historyStack = historyStacks[historyStacks.length - 1]
        if (historyStack[0].length > parsedLines[historyStacks.length - 1].length) {
            if (historyStacks.length === parsedLines.length) {
                setTimeout(() => setSolution([
                    historyStacks.map(historyStack => historyStack[0][0]).reduce((a, b) => a + b),
                    historyStacks.map(historyStack => historyStack[0][historyStack[0].length - 1]).reduce((a, b) => a + b)
                ]), 100)
            } else {
                setTimeout(() => setHistoryStacks([
                    ...historyStacks.slice(0, historyStacks.length - 1),
                    [historyStack[0]],
                    [parsedLines[historyStacks.length]]
                ]), 100)
            }
        } else {
            const bottomHistory = historyStack[historyStack.length - 1]
            let newHistoryStack: number[][]
            let timeoutCount: number
            if (all(v => v === 0, bottomHistory)) {
                newHistoryStack = [];
                [...historyStack].reverse().forEach((higher, i) => {
                    if (i > 0) {
                        const lower = newHistoryStack[i-1]
                        newHistoryStack.push([
                            higher[0] - lower[0],
                            ...higher,
                            higher[higher.length - 1] + lower[lower.length - 1]
                        ])
                    } else {
                        newHistoryStack.push([0, ...higher, 0])
                    }
                })
                newHistoryStack.reverse()
                timeoutCount = 100
            } else {
                newHistoryStack = [...historyStack, bottomHistory.slice(1).map(
                    (temp, i) => temp - bottomHistory[i]
                )]
                timeoutCount = 10
            }
            setTimeout(() => setHistoryStacks([
                ...historyStacks.slice(0, historyStacks.length - 1),
                newHistoryStack
            ]), timeoutCount)
        }
    }, [historyStacks])

    return <div className="flex flex-col gap-2 font-mono">{
        solution
        ? <div className="flex flex-row gap-4 font-bold"><div>{solution[0]}</div><div>{solution[1]}</div></div>
        : historyStacks.map((historyStack, i) => (
            <UnsolvedStack key={i} historyStack={historyStack} extended={historyStack[0].length > parsedLines[i].length} />
        ))
    }</div>
}

function parseLine(inputLine: string) {
    return inputLine.split(" ").map(s => parseInt(s))
}

function all<T>(predicate: {(arg0: T, arg1: number): boolean}, array: T[]): boolean {
    for (let i = 0; i < array.length; i++) {
        if (!predicate(array[i], i)) {
            return false
        }
    }
    return true
}