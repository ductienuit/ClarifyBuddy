# Clarify

**Trợ lý chất lượng yêu cầu cho BA/PO — biến ý tưởng mơ hồ thành BRD/PRD ký duyệt được, có điểm số, có truy vết, không bịa nghiệp vụ.**

Clarify là một *agent skill* chạy trong [Claude](https://claude.ai) (Claude Desktop, Claude.ai, hoặc Claude Code). Nó đóng vai một senior BA đồng hành: đặt đúng câu hỏi cho đúng người, soạn tài liệu đúng chuẩn, vẽ sơ đồ, dựng wireframe và **chấm điểm chất lượng** tài liệu theo một bộ 36 anti-pattern. Điều nó chưa chắc, nó hỏi; điều bạn chưa quyết, nó chờ.

> 📖 **Đọc hướng dẫn trực quan (đẹp, đầy đủ):** **https://ductienuit.github.io/ClarifyBuddy/**
> *(Trang tĩnh, tiếng Việt — what it does, hành trình 6 bước, ví dụ gửi tiết kiệm, FAQ.)*

---

## Dành cho ai?

Business Analyst và Product Owner cần soạn **BRD/PRD** chất lượng cao mà không phải bắt đầu từ trang trắng — đặc biệt mảng ngân hàng/fintech. Bạn không cần biết code.

## Clarify giải quyết gì?

| Vấn đề quen thuộc của BA | Clarify làm gì |
|---|---|
| Ngồi nhìn trang trắng, không biết hỏi gì trước | Hỏi 5 câu chặn phạm vi quan trọng nhất + bảng phương án để bạn **tick chọn** |
| AI viết tài liệu nghe hay nhưng **bịa** quy tắc, con số | Mọi điều chưa chắc đều gắn nhãn `ASSUMPTION` / `OPEN QUESTION` / `SUGGESTION` — không bao giờ tự bịa |
| Tài liệu chỉ tả "user bấm → hệ thống trả lời" | Tự soi thêm góc vận hành, kế toán, đối soát, rủi ro, bảo trì; cấu hình tham số; job chạy nền |
| Không biết tài liệu của mình "đủ tốt" chưa | Chấm **100 điểm / 10 tiêu chí**; còn lỗi nặng thì band tự chặn ở "Not ready for handoff" |
| Phải copy code sơ đồ sang web để xem, tự prompt wireframe | `export` đóng gói **Review Pack HTML** mở ra là thấy: sơ đồ render sẵn + wireframe |
| Sửa tài liệu nhiều lần, mất dấu vết quyết định | Decision Log ghi mọi quyết định; finalize tự lưu version, không đè mất bản cũ |

---

## Cài đặt (5 phút)

### Cách 1 — Claude Desktop / Claude.ai *(khuyên dùng cho BA/PO)*

1. Tải các gói skill `.zip` trong thư mục [`build/`](build/) của repo này (gói router `clarify.zip` và 8 gói lệnh chuyên biệt). Bấm vào từng file → **Download**.
2. Trong Claude: **Settings → Capabilities → Skills → Upload skill**, tải lần lượt từng `.zip` (bật *Code execution* nếu được hỏi).
3. Mở một cuộc chat và gõ tự nhiên, ví dụ: *"clarify: tôi muốn làm BRD cho tính năng gửi tiết kiệm online"*.

> Không nhớ nên dùng skill nào? Cứ chọn **`clarify`** (router) — nó tự chẩn đoán nhu cầu và định tuyến cho bạn.

### Cách 2 — Claude Code *(cho người làm việc trong repo)*

1. Clone repo này về và mở trong [Claude Code](https://docs.claude.com/en/docs/claude-code):
   ```bash
   git clone https://github.com/ductienuit/ClarifyBuddy.git
   ```
2. Claude Code tự nhận 8 slash command dưới đây. Mọi sản phẩm được ghi vào thư mục `clarify-output/`.

---

## Dùng từng bước (step by step)

Hành trình chuẩn: **4 bước bắt buộc + 2 bước tuỳ chọn.** Ví dụ xuyên suốt: *"tính năng mở sổ tiết kiệm online"*.

**1. Định hình ý tưởng — `/clarify:from-idea`**
Mô tả ý tưởng bằng một câu. Clarify lập **Document Profile** (vai trò BA/PO · chuẩn BRD/PRD · domain · ngôn ngữ) rồi hỏi tối đa 5 câu chặn phạm vi và đưa **bảng phương án (Variant Matrix)** để bạn chọn. Bạn nhận về bản nháp BRD/PRD + một **Answer Sheet** (khối câu hỏi có mã `Q1`, `A1`, `S1`, `V1`… để bạn trả lời) + **Elicitation Pack** (câu hỏi gom theo *người cần hỏi*).

**2. Trả lời & chốt — `/clarify:improve answers`**
Copy Answer Sheet, điền sau mỗi mã, dán lại. Clarify áp từng quyết định: câu trả lời thành rule đã chốt, đề xuất được duyệt vào phạm vi. Mọi quyết định tự ghi vào **Decision Log**.

**3. (Tuỳ chọn) Lớp build-ready — `/clarify:from-spec`**
Khi cần bàn giao Dev/QA: thêm điểm audit, user stories, acceptance criteria, test, phân tích API/dữ liệu, ma trận truy vết. Bỏ qua nếu chỉ cần ký duyệt nghiệp vụ.

**4. Chốt tài liệu — `/clarify:finalize brd`** (hoặc `prd`)
Biên soạn tài liệu cuối chuẩn ký duyệt: Document control + Change history, Executive summary, Functional Flows theo nghiệp vụ, bảng lỗi & thông điệp khách hàng, truy vết, Sign-off blockers. Chạy lại không đè mất bản cũ (tự lưu `final-brd.v1.md`, tăng version).

**5. Đóng gói review — `/clarify:export`**
Tạo **Review Pack HTML** (`review-pack/index.html`): mở bằng trình duyệt là thấy sơ đồ render sẵn, sơ đồ điều hướng màn hình, wireframe low-fi, bảng lỗi, truy vết, checklist. Gửi một file cho cả PO/Design/Dev/QA.

**6. Khi cần — `status`, `handoff`, `change-request`**
`/clarify:status` cho biết bạn đang ở đâu, còn gì tồn đọng. `/clarify:handoff` xuất gói Dev + gói QA. `/clarify:improve change-request` phân tích tác động của một thay đổi qua chuỗi truy vết.

---

## 8 lệnh (The 8 commands)

| Lệnh | Dùng khi |
|---|---|
| `/clarify:from-idea` | Chỉ có một ý tưởng / mô tả ngắn |
| `/clarify:improve` | Trả lời Answer Sheet (`answers`), nâng cấp một mục, hoặc phân tích `change-request` |
| `/clarify:from-spec` | Có sẵn PRD/BRD, hoặc cần lớp build-ready cho Dev/QA |
| `/clarify:audit` | Chỉ muốn chấm điểm + danh sách lỗi |
| `/clarify:handoff` | Bàn giao Dev/QA |
| `/clarify:finalize` | Chốt tài liệu BRD/PRD ký duyệt |
| `/clarify:export` | Đóng gói Review Pack trực quan |
| `/clarify:status` | Xem mình đang ở đâu trong pipeline |

---

## Nguyên tắc bất biến

**Không bịa nghiệp vụ.** Con số, quy tắc, mã lỗi là quyết định của tổ chức bạn — Clarify đề xuất khung, gắn nhãn những gì chưa chắc, và chỉ ra *cần hỏi ai*. Chất lượng tài liệu cuối phụ thuộc nhiều nhất vào việc bạn trả lời Answer Sheet đầy đủ.

## Cấu trúc repo

```
.claude/commands/clarify/   # 8 slash-command adapters (Claude Code)
.clarify/                   # bộ skill pack:
  workflows/                # quy trình cho từng lệnh
  engine/                   # 16 imperative engines
  templates/                # 22 output shapes
  anti-patterns/            # 36-entry anti-pattern catalog + rubric chấm điểm
  domain-packs/             # gói kiến thức ngành (fintech, ecommerce, saas-b2b)
skills/                     # nguồn cho từng gói skill chuyên biệt (Claude Desktop)
build/                      # 9 file .zip cài đặt sẵn cho Claude Desktop
docs/                       # trang hướng dẫn (GitHub Pages)
examples/                   # ví dụ minh hoạ
```

Đóng gói lại các zip sau khi sửa skill (cần PowerShell): `pwsh ./build-skill.ps1`.
Chi tiết đóng góp: [CONTRIBUTING.md](CONTRIBUTING.md) · Lịch sử thay đổi: [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE)
