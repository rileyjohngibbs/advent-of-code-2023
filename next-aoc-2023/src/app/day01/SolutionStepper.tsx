'use client'

import { useState } from "react"

import { SolutionState, LineState } from "./types"
import LeftScan from "./LeftScan"
import RightScan from "./RightScan"
import ConcatenateDigits from "./ConcatenateDigits"
import RowSum from "./RowSum"

/*
1. Scan each line from left until first digit is found.
2. Scan each line from right until first digit is found.
3. Concatenate the digits and interpret as a number.
4. Add the numbers together.

1. Scan each line from left until first number name or digit is found.
*/

interface Props { inputLines: string[] }


export default function SolutionStepper({ inputLines }: Props) {
    const [problemPart, setProblemPart] = useState<1|2>(1)
    const [solutionState, setSolutionState] = useState<SolutionState>(
        new SolutionState(inputLines.map(line => new LineState(line)))
    )
    
    if (solutionState.solution !== null) {
        setProblemPart(problemPart === 1 ? 2 : 1)
        setSolutionState(new SolutionState(inputLines.map(line => new LineState(line))))
    } else if (solutionState.lineStates[0].formedNumber !== null) {
        const nextStateSetter = (solution: number) => {
            setSolutionState(new SolutionState(solutionState.lineStates, solution))
        }
        return <RowSum lineStates={solutionState.lineStates} nextStateSetter={nextStateSetter} />
    } else if (solutionState.lineStates[0].rightDigit !== null) {
        const nextStateSetter = (formedNumbers: number[]) => {
            setSolutionState(new SolutionState(solutionState.lineStates.map(
                ({line, leftDigit, rightDigit}, i) => new LineState(line, leftDigit, rightDigit, formedNumbers[i])
            )))
        }
        return <ConcatenateDigits lineStates={solutionState.lineStates} nextStateSetter={nextStateSetter} />
    } else if (solutionState.lineStates[0].leftDigit !== null) {
        return <LeftScan solutionState={solutionState} problemPart={problemPart} setSolutionState={setSolutionState} />
    } else {
        return <LeftScan solutionState={solutionState} problemPart={problemPart} setSolutionState={setSolutionState} />
    }
}