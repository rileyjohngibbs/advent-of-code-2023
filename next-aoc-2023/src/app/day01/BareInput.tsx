interface Props { lines: string[], nextStateSetter: {(value: string[]): void}}

export default function BareInput({ lines, nextStateSetter }: Props) {
    setTimeout(() => nextStateSetter(lines), 2000)
    return lines.map((line, i) => <div key={i}>{line}</div>)
}