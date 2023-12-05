interface Props {
    fullyScannedLines: { leftDigit: number, rightDigit: number }[], nextStateSetter: {(value: number[]): void}
}

export default function ConcatenateDigits({ fullyScannedLines, nextStateSetter }: Props) {
    const calibrationValues = fullyScannedLines.map(
        ({leftDigit, rightDigit}) => leftDigit * 10 + rightDigit
    )
    setTimeout(() => nextStateSetter(calibrationValues), 2000)
    return calibrationValues.map((calVal, i) => <div key={i}>{calVal}</div>)
}