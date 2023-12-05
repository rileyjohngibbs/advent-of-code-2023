'use client'

import { useEffect, useState } from "react"

import BareInput from "./BareInput"
import LeftScan from "./LeftScan"
import RightScan from "./RightScan"
import ConcatenateDigits from "./ConcatenateDigits"
import RowSum from "./RowSum"

/*
1. Scan each line from left until first digit is found.
    1. (line: string, index: number, leftDigit: number?, incompleteSetter: {(): null}) => {line, index, leftDigit}
2. Scan each line from right until first digit is found.
3. Concatenate the digits and interpret as a number.
4. Add the numbers together.
*/

interface Props { inputLines: string[] }

export default function SolutionStepper({ inputLines }: Props) {
    const [bareInput, setBareInput] = useState<string[]>()
    const [leftScan, setLeftScan] = useState<{line: string, leftDigit: number}[]>()
    const [rightScan, setRightScan] = useState<{line: string, leftDigit: number, rightDigit: number}[]>()
    const [concenateDigits, setConcatenateDigits] = useState<number[]>()
    const [rowSum, setRowSum] = useState<number>()
    
    if (rowSum !== undefined) {
        [setBareInput, setLeftScan, setRightScan, setConcatenateDigits, setRowSum].forEach(
            (setter) => setter(undefined)
        )
    } 
    if (concenateDigits !== undefined) {
        return <RowSum calibrationValues={concenateDigits} nextStateSetter={setRowSum} />
    } else if (rightScan !== undefined) {
        return <ConcatenateDigits fullyScannedLines={rightScan} nextStateSetter={setConcatenateDigits} />
    } else if (leftScan !== undefined) {
        return <RightScan leftScannedLines={leftScan} nextStateSetter={setRightScan} />
    } else if (bareInput !== undefined) {
        return <LeftScan lines={bareInput} nextStateSetter={setLeftScan} />
    } else {
        return <BareInput lines={inputLines} nextStateSetter={setBareInput} />
    }
}