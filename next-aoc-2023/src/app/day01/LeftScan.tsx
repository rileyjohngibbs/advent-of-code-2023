interface Result { line: string, leftDigit: number }
interface Props {
    lines: string[], nextStateSetter: {(value: Result[]): void}
}

export default function LeftScan({ lines, nextStateSetter }: Props) {
    const results = lines.map((line) => {
        const digit = line.split("").find(s => !isNaN(parseInt(s)))
        return { line, leftDigit: digit ? parseInt(digit) : -1}
    })
    setTimeout(() => nextStateSetter(results), 2000)
    return results.map(({line, leftDigit}, i) => <div key={i}>{leftDigit} {line}</div>)
}