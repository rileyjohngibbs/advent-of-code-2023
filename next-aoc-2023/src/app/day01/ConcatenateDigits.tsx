interface Props {
    lineStates: { leftDigit: number | null, rightDigit: number | null }[], nextStateSetter: {(value: number[]): void}
}

export default function ConcatenateDigits({ lineStates, nextStateSetter }: Props) {
    const calibrationValues = lineStates.map(
        ({leftDigit, rightDigit}) => (leftDigit ?? 0) * 10 + (rightDigit ?? 0)
    )
    setTimeout(() => nextStateSetter(calibrationValues), 2000)
    return calibrationValues.map((calVal, i) => <div key={i}>{calVal}</div>)
}