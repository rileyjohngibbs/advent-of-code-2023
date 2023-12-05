import { useState, useEffect } from "react"

interface Result { line: string, leftDigit: number }
interface Props {
    lines: string[], nextStateSetter: {(value: Result[]): void}
}

export default function LeftScan({ lines, nextStateSetter }: Props) {
    const [rows, setRows] = useState<{counter: number, digit: number | null}[]>(
        Array(lines.length).fill(null).map(() => {return {counter: 0, digit: null}})
    )
    useEffect(() => {
        if (rows.findIndex(row => row.digit === null) === -1) {
            setTimeout(() => nextStateSetter(rows.map(
                ({digit}, i) => {return {line: lines[i], leftDigit: digit ?? 0}}
            )), 2000)
        } else {
            const newRows: {counter: number, digit: number | null}[] = Array(lines.length)
            lines.forEach((line, i) => {
                const row = rows[i]
                if (row.counter === null) {
                    newRows[i] = row
                } else {
                    const parsed = parseInt(line[row.counter])
                    if (!isNaN(parsed)) {
                        newRows[i] = {counter: row.counter, digit: parsed}
                    } else {
                        newRows[i] = {counter: row.counter + 1, digit: null}
                    }
                }
            })
            setTimeout(() => setRows(newRows), 100)
        }
    }, [rows])

    return rows.map(({counter, digit}, i) => {
        return <div key={i}>{digit ?? "_"} {
            lines[i].split("").map(
                (c, j) => j === counter ? <span key="j" className="font-bold">{c}</span> : c
            )
        }</div>
    })
}