'use client'

import { useEffect, useState } from "react"

interface Props { lineStates: {formedNumber: number | null}[], nextStateSetter: {(value: number): void} }

export default function RowSum({ lineStates, nextStateSetter }: Props) {
    const formedNumbers = lineStates.map(({formedNumber}) => formedNumber)

    const [remainingRows, setRemainingRows] = useState<(number | null)[]>(formedNumbers)
    const [total, setTotal] = useState<number>()

    const duration = formedNumbers.length * 5
    useEffect(() => {
        const index = remainingRows.findIndex(x => x !== null)
        if (index !== -1) {
            setTimeout(() => {
                setTotal((total ?? 0) + (remainingRows[index] ?? 0))
                setRemainingRows(remainingRows.map((v, i) => i === index ? null : v)), 10
            })
        } else {
            setTimeout(() => nextStateSetter(total ?? 0), 2000)
        }
    }, remainingRows)
    
    return <div>
        <div>{total}</div>
        {remainingRows.map((row, i) => <div key={i}>{row}</div>)}
    </div>
}