import { useState, useEffect } from "react"

interface Result { line: string, leftDigit: number, rightDigit: number }
interface Props {
    leftScannedLines: {line: string, leftDigit: number}[], nextStateSetter: {(value: Result[]): void}
}

export default function RightScan({ leftScannedLines, nextStateSetter }: Props) {
    const [rows, setRows] = useState<{counter: number, digit: number | null}[]>(
        Array(leftScannedLines.length).fill(null).map(() => {return {counter: 1, digit: null}})
    )
    useEffect(() => {
        if (rows.findIndex(({digit}) => digit === null) === -1) {
            nextStateSetter(rows.map((row, i) => {
                const {line, leftDigit} = leftScannedLines[i]
                return {line: line, leftDigit: leftDigit, rightDigit: row.digit ?? 0}
            }))
        } else {
            const newRows: {counter: number, digit: number | null}[] = Array(leftScannedLines.length)
            rows.forEach((row, i) => {
                const {line} = leftScannedLines[i]
                const parsed = parseInt(line[line.length - row.counter])
                if (!isNaN(parsed)) {
                    newRows[i] = {counter: row.counter, digit: parsed}
                } else {
                    newRows[i] = {counter: row.counter + 1, digit: null}
                }
            })
            setTimeout(() => setRows(newRows), 100)
        }
    }, [rows])

    return rows.map(({counter, digit}, i) => {
        const {line, leftDigit} = leftScannedLines[i]
        return <div key={i}>{leftDigit}{digit ?? "_"} {
            line.split("").map(
                (c, j) => j === line.length - counter ? <span key="j" className="font-bold">{c}</span> : c
            )
        }</div>
    })
}