interface Result { line: string, leftDigit: number, rightDigit: number }
interface Props {
    leftScannedLines: {line: string, leftDigit: number}[], nextStateSetter: {(value: Result[]): void}
}

export default function RightScan({ leftScannedLines, nextStateSetter }: Props) {
    const results = leftScannedLines.map(({ line, leftDigit }) => {
        const digit = line.split("").reverse().find(s => !isNaN(parseInt(s)))
        return { line, leftDigit, rightDigit: digit ? parseInt(digit) : -1}
    })
    setTimeout(() => nextStateSetter(results), 2000)
    return results.map(
        ({line, leftDigit, rightDigit}, i) => <div key={i}>{leftDigit} {line} {rightDigit}</div>
    )
}