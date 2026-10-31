# Draw Music Studio — Terms & Privacy

Tài liệu tiếng Anh cho **Draw Music Studio**, package `com.drawmusic.studio`, version 1.0, nhà phát triển KhoaiStore, email hvdevelopapplication@gmail.com. Đối chiếu mã nguồn ngày 31/10/2026.

- Privacy: https://hoangvietonline.github.io/Draw_Music_Privacy_Policy/
- Terms: https://hoangvietonline.github.io/Draw_Music_Privacy_Policy/terms.html
- GitHub: https://github.com/hoangvietonline/Draw_Music_Privacy_Policy

## Repo độc lập trong project

Thư mục `Draw Music Legal/` nằm trong project Draw Music nhưng có `.git` riêng và được repo Android bỏ qua. Chỉ commit/push từ thư mục này để cập nhật website. GitHub Pages dùng main, thư mục gốc.

## Đóng gói

Chạy `python3 sync_offline.py` từ thư mục này sau khi sửa nội dung. Script nhúng CSS và sao chép hai trang vào assets `privacy-local.html`, `terms-local.html`. Android tự đóng gói các assets vào APK/AAB. Settings có hai mục Privacy và Terms riêng: ưu tiên URL GitHub Pages, tự chuyển sang bản đóng gói nếu lỗi mạng, lỗi HTTP hoặc tải quá 5 giây. Internet chỉ dùng để tải trang pháp lý; nội dung sáng tác vẫn xử lý trên máy. Không cần mạng để đọc hai tài liệu.

## Phạm vi

Mô tả đúng app offline: local projects/Room, DataStore, background photo qua picker hoặc camera app bên ngoài, ảnh nhúng JSON, WAV/MIDI/MP4, xuất/chia sẻ, retention/deletion, không ads/analytics/billing/login; allowBackup=false. Không sao chép các tuyên bố AdMob, camera preview, ML Kit hoặc subscriptions của AR Drawing.

Tên nhà phát triển/email dùng thông tin KhoaiStore đã có trong bộ tài liệu tham chiếu cùng chủ tài khoản; đối chiếu với store listing khi phát hành. Chưa kiểm tra cấu hình Play Console hoặc lưu lượng của AAB cuối cùng.

Nguồn chính thức: [Google Play User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en), [Android backup](https://developer.android.com/identity/data/autobackup), [GitHub privacy](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
