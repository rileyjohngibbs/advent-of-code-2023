import { useState, useEffect } from "react"
import { LineState, SolutionState } from "./types"

const ALL_TOKENS = [
    {name: 'one', value: 1},
    {name: 'two', value: 2},
    {name: 'three', value: 3},
    {name: 'four', value: 4},
    {name: 'five', value: 5},
    {name: 'six', value: 6},
    {name: 'seven', value: 7},
    {name: 'eight', value: 8},
    {name: 'nine', value: 9},
    {name: '1', value: 1},
    {name: '2', value: 2},
    {name: '3', value: 3},
    {name: '4', value: 4},
    {name: '5', value: 5},
    {name: '6', value: 6},
    {name: '7', value: 7},
    {name: '8', value: 8},
    {name: '9', value: 9},
]
interface Props {
    solutionState: SolutionState, problemPart: 1 | 2, setSolutionState: {(value: SolutionState): void}
}
interface LineProgress {
    line: string,
    digit: number | null,
    left: number,
    right: number,
    tokenIndices: number[],
}

const highlight = (text: string, left: number, right: number, reversed: boolean) => {
    const hleft = reversed ? text.length - right : left
    const hright = reversed ? text.length - left : right
    return <>
        {text.slice(0, hleft)}
        <span className="font-bold">{text.slice(hleft, hright)}</span>
        {text.slice(hright)}
    </>
}

export default function LeftScan({solutionState: {lineStates}, problemPart, setSolutionState}: Props) {
    const [scanRight, setScanRight] = useState(lineStates[0].leftDigit !== null)
    const [leftDigits, setLeftDigits] = useState<(number | null)[]>(Array(lineStates.length).fill(null))
    const lines = lineStates.map(ls => ls.line)
    const number_tokens = ALL_TOKENS.filter(({name}) => problemPart === 2 || name.length === 1)
    const [linesProgress, setLinesProgress] = useState<LineProgress[]>(lines.map(line => {
        return {line, left: 0, digit: null, right: 1, tokenIndices: number_tokens.map(
            ({name}, i) => {
                const nameSlice = name.slice(
                    scanRight ? name.length - 1 : 0, scanRight ? name.length : 1
                )
                const lineSlice = line.slice(
                    scanRight ? line.length - 1 : 0, scanRight ? line.length : 1
                )
                return nameSlice === lineSlice ? i : -1
            }
        ).filter(i => i > -1)}
    }))

    useEffect(() => {
        if (linesProgress.findIndex(({digit}) => digit === null) === -1) {
            if (leftDigits[0] === null) {
                setTimeout(() => {
                    setLeftDigits(linesProgress.map(lp => lp.digit))
                    setScanRight(true)
                    setLinesProgress(linesProgress.map(({line}) => {
                        return {line, digit: null, left: -1, right: 0, tokenIndices: []}
                    }))
                }, 2000)
            } else {
                setTimeout(() => setSolutionState(new SolutionState(
                    linesProgress.map(({digit}, i) => new LineState(
                        lines[i],
                        scanRight ? lineStates[i].leftDigit : digit,
                        scanRight ? digit : null
                    ))
                )), 2000)
            }
        } else {
            const linesNext = linesProgress.map(lineStepper(number_tokens, scanRight))
            setTimeout(() => {setLinesProgress(linesNext)}, 100)
        }
    }, [linesProgress])

    return linesProgress.map(({line, digit, left, right, tokenIndices: tokens}, i) => {
        const tokensSet = new Set(tokens)
        return <div key={i} className="flex flex-row gap-3">
            <div>{digit ?? "_"}</div>
            <div>{highlight(line, left, right, scanRight)}</div>
            {number_tokens.map(
                (value, j) => {
                    const matches = tokensSet.has(j)
                    return <div key={j} className={matches ? '' : 'opacity-30'}>
                        {matches ? highlight(value.name, 0, right - left, scanRight) : value.name}
                    </div>
                }
            )}
        </div>
    })
}

function lineStepper(number_tokens: {name: string, value: number}[], scanRight: boolean) {
    const lineStep = (lineProgress: LineProgress) => {
        if (lineProgress.digit !== null) return lineProgress
        const {line} = lineProgress
        const fullMatchTokenIndex = lineProgress.tokenIndices.find(
            token_index => number_tokens[token_index].name.length === lineProgress.right - lineProgress.left
        )
        if (fullMatchTokenIndex !== undefined) {
            const digit = number_tokens[fullMatchTokenIndex].value
            const {left, right, tokenIndices} = lineProgress
            return {line, digit, left, right, tokenIndices}
        } else {
            const {digit} = lineProgress
            const [left, right, currentTokenIndices] = (
                lineProgress.tokenIndices.length
                ? [lineProgress.left, lineProgress.right + 1, lineProgress.tokenIndices]
                : [lineProgress.left + 1, lineProgress.left + 2, number_tokens.map((_v, i) => i)]
            )
            const subLine = line.slice(
                scanRight ? line.length - right : left,
                scanRight ? line.length - left : right
            )
            const length = right - left
            const tokenIndices = currentTokenIndices.map(
                index => {
                    const tokenName = number_tokens[index].name
                    const slice = tokenName.slice(
                        scanRight ? tokenName.length - length : 0,
                        scanRight ? tokenName.length : length
                    )
                    return slice === subLine ? index : -1
                }
            ).filter(i => i > -1)
            return {line, digit, left, right, tokenIndices}
        }
    }
    return lineStep
}